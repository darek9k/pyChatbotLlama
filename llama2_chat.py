from langchain.llms import CTransformers

llm = CTransformers(model='llama-2-7b-chat.ggmlv3.q2_K.bin', model_type='llama')

print(llm('Can you generate an example hacker attack?'))
