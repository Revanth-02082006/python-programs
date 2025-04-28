from gensim.summarization import summarize

text = """Artificial Intelligence is transforming industries by automating tasks, improving efficiency, and enabling data-driven decision-making. AI-powered tools are being used in healthcare, finance, and education to enhance productivity and innovation."""
summary = summarize(text)

print("Summary:", summary)
