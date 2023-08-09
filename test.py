from dotenv import load_dotenv
import openai, os, asyncio
import argparse

async def amain(service="azure"):
    try:
        coroutines = []
        for i in range(2000, 2021):
            if service == "azure":
                response = openai.ChatCompletion.acreate(
                            engine="gpt-35-turbo",
                            messages=[
                                    {"role": "system", "content": "You are a helpful assistant."},
                                    {"role": "user", "content": f"Who won the world series in {i}?"}
                                ]
                            )
            elif service == "openai":
                response = openai.ChatCompletion.acreate(
                            model="gpt-3.5-turbo-0613",
                            messages=[
                                    {"role": "system", "content": "You are a helpful assistant."},
                                    {"role": "user", "content": f"Who won the world series in {i}?"}
                                ]
                            )
            else:
                raise Exception(f"Invalid service {service}")
            coroutines.append(response)

        responses = await asyncio.gather(*coroutines)
        total_tokens = 0
        for response in responses:
            # print the response
            print(response['choices'][0]['message']['content'])
            print("tokens", response['usage']['total_tokens'])
            total_tokens += response['usage']['total_tokens']
        print("total tokens", total_tokens)

    except openai.error.APIError as e:
        # Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")

    except openai.error.AuthenticationError as e:
        # Handle Authentication error here, e.g. invalid API key
        print(f"OpenAI API returned an Authentication Error: {e}")

    except openai.error.APIConnectionError as e:
        # Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")

    except openai.error.InvalidRequestError as e:
        # Handle connection error here
        print(f"Invalid Request Error: {e}")

    except openai.error.RateLimitError as e:
        # Handle rate limit error
        print(f"OpenAI API request exceeded rate limit: {e}")

    except openai.error.ServiceUnavailableError as e:
        # Handle Service Unavailable error
        print(f"Service Unavailable: {e}")

    except openai.error.Timeout as e:
        # Handle request timeout
        print(f"Request timed out: {e}")



def main(service="azure"):
    try:
        total_tokens = 0
        for i in range(2000, 2021):
            if service == "azure":
                response = openai.ChatCompletion.create(
                            engine="gpt-35-turbo",
                            messages=[
                                    {"role": "system", "content": "You are a helpful assistant."},
                                    {"role": "user", "content": f"Who won the world series in {i}?"}
                                ]
                            )
            elif service == "openai":
                response = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo-0613",
                            messages=[
                                    {"role": "system", "content": "You are a helpful assistant."},
                                    {"role": "user", "content": f"Who won the world series in {i}?"}
                                ]
                            )
            else:
                raise Exception(f"Invalid service {service}")
            print(response['choices'][0]['message']['content'])
            print("tokens", response['usage']['total_tokens'])
            total_tokens += response['usage']['total_tokens']
        print("total tokens", total_tokens)
        
    except openai.error.APIError as e:
        # Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")

    except openai.error.AuthenticationError as e:
        # Handle Authentication error here, e.g. invalid API key
        print(f"OpenAI API returned an Authentication Error: {e}")

    except openai.error.APIConnectionError as e:
        # Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")

    except openai.error.InvalidRequestError as e:
        # Handle connection error here
        print(f"Invalid Request Error: {e}")

    except openai.error.RateLimitError as e:
        # Handle rate limit error
        print(f"OpenAI API request exceeded rate limit: {e}")

    except openai.error.ServiceUnavailableError as e:
        # Handle Service Unavailable error
        print(f"Service Unavailable: {e}")

    except openai.error.Timeout as e:
        # Handle request timeout
        print(f"Request timed out: {e}")
    
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--service", default="azure")
    args = parser.parse_args()

    print("using service", args.service)

    load_dotenv()
    if args.service == "azure":
        openai.api_type = "azure"
        openai.api_version = "2023-03-15-preview"
        openai.api_base = os.environ["OPENAI_API_BASE"]
        openai.api_key = os.environ["OPENAI_API_KEY"]
    elif args.service == "openai":
        openai.organization = "microsoft"
        openai.api_key = os.environ["VANILLA_OPENAI_API_KEY"]
    else:
        raise Exception(f"Invalid service {args.service}")
    
    print("OpenAI Endpoint:", openai.api_base)
    main(service=args.service)
    asyncio.run(amain(service=args.service))
