# Mastering OpenAI Python APIs: Unleash the Power of GPT4

Mastering OpenAI Python APIs: Unleash the Power of GPT4 by Colt Steele

## File Structure

# Details

<details open>
  <summary>Click to Contract/Expend</summary>

## Section 1: Introduction

### 4. Let's Talk About GPT

GPT : Generative Pre-Trained Transformer

#### Training

- GPT-3 was trained on over 45TB of text data:
  - A quality-filtered subset of the CommonDrawl Dataset
  - An expanded version of the Webtest dataset
    - All outbound links from Reddit with >3 Karma
  - Two databases of online books
  - English-language Wikipedia
- Nearly 500 billion tokens of training data
- Open AI has not released information on the training of GPT-4

### 5. OPTIONAL: The Transformer Architecture

#### How?

- GPT-4 is based on a type of neural network called a **transformer**
  - Transformers are a deep learning model that excel at processing sequential data (like natural language text)

#### Neural Networks

- Convolutional Neural Networks
  - work great for analyzing images
- Recurrent Neural Networks
  - work well at text processing and translation
- Transformers

##### Recurrent Neural Networks

RNNs work sequentailly, processing text one word at a time, but they have some problems

- They're not great at analyzing large pieces of text
- They're slow to train. This means they can't be trained on huge amounts of data easily
- Training can't be parallelized because they process sequentially

#### Transformers

- Transformers are relatively recent approach (2017)
- Transformers process the entire input at once, rather than sequentially, meaning there is less risk of "forgetting" previous context
- This means they can be trained in parallel

Transformers introduced a couple key innovations

- Positional Encoding
- Self attention

## Section 2: Getting Started

### 10. Our First Completion Request

```sh
poetry init
poetry add jupyter
poetry add openai
```

### 12. Hiding Our API Key

```sh
poetry add python-dotenv
```

### 13. Understanding Tokens

- [OpenAI API - Tokenizer](https://platform.openai.com/tokenizer)

### 15. Stop Sequences

- [Completion parameters examples](https://github.com/pcsmomo/openai-api-python-andrei/blob/main/02-dive-into-openai-api/14-completion-parameters.ipynb)
- [Completion parameters Doc](https://platform.openai.com/docs/api-reference/completions/create)

### 16. N and Echo

echo option doesn't add up the completion_tokens which means no extra cost

</details>
