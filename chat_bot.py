
from transformers import AutoTokenizer
import tiktoken
import dotenv
import os
import time
from openai import OpenAI

dotenv.load_dotenv()


class ChatBot:
    def __init__(self):
        self.llm = OpenAI(
            api_key=os.getenv('GROQ_API_KEY'),
            base_url='https://api.groq.com/openai/v1'
        )

        self.messages = [
            {
                'role': 'system',
                'content': '''You are a helpful assistant. Your name is Vikie.
                Introduce youself in first messages. Give short anwers'''
            }
        ]

        self.total_tokens = 0
        self.input_tokens = 0
        self.output_tokens = 0
        self.iteration = 0

    def trim_messages(self, max_number=4):
        if len(self.messages) < max_number:
            return
        system_messages = [m for m in self.messages if m['role'] == 'system']
        other_messages = [m for m in self.messages if m['role'] != 'system']
        trimmed_messages = other_messages[-max_number:]
        self.messages = [*system_messages, *trimmed_messages]

    def summarize_messages(self):
        if self.iteration % 5 != 0:
            return
        system_messages = [m for m in self.messages if m['role'] == 'system']
        other_messages = [m for m in self.messages if m['role'] != 'system']

        early_messages, last_messages = (
            other_messages[0:5], other_messages[5:])
        response = self.llm.chat.completions.create(
            model='openai/gpt-oss-20b',
            messages=[
                {
                    'role': 'system',
                    'content': 'Summarize these messages concisely,keeping facts and decisions.'
                }, *early_messages
            ],
        )

        summarized_message = {
            'role': 'system',
            'content': f'''This is a summary of the five early messages:
            {response.choices[0].message.content}'''
        }
        self.messages = [*system_messages, summarized_message, *last_messages]
        print('Summarization was successful')

    def bot(self, message):

        self.messages.append({
            'role': 'user',
            'content': message
        })

        response = self.llm.chat.completions.create(
            model='openai/gpt-oss-20b',
            messages=self.messages,
            stream=True,
            stream_options={"include_usage": True}
        )

        response_text = ''

        for chunk in response:
            if chunk.choices:
                delta = chunk.choices[0].delta.content

                if delta:
                    print(delta, end='', flush=True)
                    response_text += delta
                    time.sleep(0.05)

            if chunk.usage:
                self.total_tokens += chunk.usage.total_tokens
                self.input_tokens += chunk.usage.prompt_tokens
                self.output_tokens += chunk.usage.completion_tokens

        print()

        self.messages.append({
            'role': 'assistant',
            'content': response_text
        })
        self.summarize_messages()
        return response_text

    def chat(self):
        encoding = AutoTokenizer.from_pretrained('openai/gpt-oss-20b')

        while True:
            self.iteration += 1
            user_input = input('Ask Something (q to Quit) :').strip().lower()

            if user_input == 'q':
                print('Thank You')
                break

            token_count = len(encoding.encode(user_input))

            if token_count > 10:
                print('Your prompt exceeds the limit. Try again!')
                continue

            if self.total_tokens > 12000:
                print('Unfortunately,token limit exceeded!')
                break

            self.bot(user_input)

    def report(self):
        for message in self.messages:
            print(message)

        print(f'Consumed Tokens: {self.total_tokens}')
        print(f'${(self.input_tokens*0.05 + self.output_tokens*0.08)/1_000_000}')


def main():
    bot = ChatBot()
    bot.chat()
    bot.report()


if __name__ == '__main__':
    main()
