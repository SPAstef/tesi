import openai

openai.api_key = "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"

response = openai.Image.create(
    prompt="dad birthday gift card",
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)
