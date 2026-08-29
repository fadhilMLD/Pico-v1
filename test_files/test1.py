from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="OptGear/Opt.Gear-1M",
    trust_remote_code=True
)

result = pipe(
    "User: turn on the red LED and show 'hello' on the screen\nModel:",
    max_new_tokens=40,
    temperature=0.1
)

print(result[0]["generated_text"])