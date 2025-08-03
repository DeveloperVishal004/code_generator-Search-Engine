import streamlit as st
from transformers import T5Tokenizer,T5ForConditionalGeneration


model=T5ForConditionalGeneration.from_pretrained('t5_finetuned_model')
tokenizer=T5Tokenizer.from_pretrained('t5_finetuned_model')


def generate_code(query):
 query= query.lower()
 input_ids=tokenizer.encode('generate code:'+query,return_tensors='pt',truncation=True,max_length=128).to(device)
 output=model.generate(input_ids,max_length=128,num_beams=4,early_stopping=True)
 generated_code=tokenizer.decode(output[0],skip_special_tokens=True)
 return generated_code

#ui -->Streamlit app
st.title("Code Generation using Fine tuned model")
query=st.text_input('Enter your query here...')
#Button to trigger code generation
if st.button('Generate Code'):
    if query:
        code=generate_code(query)
        st.subheader('Generated Code')
        st.code(code,language='python')
    else:
        st.warning('Please enter a query to generate code. ')
