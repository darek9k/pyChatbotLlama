# pyChatbotLlama
My first chatbot for generating tests from API documentation.

# API test generator

## Overview

The following repo contains a Streamlit application to generate automated tests for API services.

## Usage

1. Enter the required information, such as selecting the type of framework and providing the content of a JSON file.
2. Click on the "Generuj testy" button to initiate the test generation process.
3. The generated tests will be displayed, and a success message will indicate completion.

## Requirements

To use the generator, make sure to have the following dependencies:
- openai
- streamlit

Install the dependencies using pip:

```
pip install openai streamlit
```

## Usage Example

```python
import openai
import streamlit as st

st.title("Generator API testów")
openai.api_key = "######"
language = st.selectbox("Wybierz rodzaj frameworka", ("RestAssured","RestSharp"))

json = st.text_area("Wprowadź zawartoś pliku JSON")

if st.button("Generuj testy"):
    with st.spinner("Generowanie testów ..."):
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Jesteś asystentem testera automatycznego pomożesz mi wygenerować testy API"
                },
                {
                    "role": "user",
                    "content": "Wygeneruj testy automatyczne w " + language + " dla serwisów z pliku Json: "+json
                }
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

    if language == "RestAssured":
        st.code(response.choices[0].message.content, language='csharp')
    else:
        st.code(response.choices[0].message.content, language='java')

    st.success("Testy zostały wygenerowane")
```

