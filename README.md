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

## Section 3: Prompt Engineering

### 18. The Elements of a Good Prompt

Prompt Design

- Main Instructions - a task you want the model to perform
- Data - any input data (if necessary)
- Output instructions - what type of output do you want? What format?

#### Tips

##### Provide clear instructions

```
Complete the sentence: Humans are

Humans are
```

##### Use a separator to designate instructions and input

```
"""Instruction"""
Translate the text below to French:

Text: "I am a huge idiot"
```

##### Reduce "fluffy" language. Be precise

```
In 3-4 sentences, explain the role of the Supreme Court in US politics. The explanation should be geared towards middle-schoolers
```

### 19. Controlling The Output Format

##### Be specific about your designer output

```
Extract the place names in the following

Desired format:
Places: <comma_separated_list_of_places>

Input: "Airbnb, Inc.is an American San Francisco-based company. The company is credited with revolutionizing the tourism industry however it has also been the subject of intense criticism by residents of tourism hotspot cities like Barcelona, Venice, etc. for enabling an unaffordable increase in home rents, and for a lack of regulation."
```

```
Extract the place names in the following

Desired format: JSON array of palce names

Input: " Airbnb, Inc.is an American San Francisco-based company. The company is credited with revolutionizing the tourism industry however it has also been the subject of intense criticism by residents of tourism hotspot cities like Barcelona, Venice, etc. for enabling an unaffordable increase in home rents, and for a lack of regulation."

Answer:
```

```
Generate a list of the top 5 most populated countries on earth with their population

Desired format: JSON object with country name as the key and population as the value
```

### 20. Summarization Prompts

```
Summarize the following text

Desired format: 2-3 sentences of text

Input:
Alaska (/əˈlæskə/ (listen) ə-LAS-kə) is a U.S. state on the northwest extremity of North America. A semi-exclave of the U.S., it borders British Columbia and Yukon in Canada to the east, and it shares a western maritime border in the Bering Strait with the Russian Federation's Chukotka Autonomous Okrug. To the north are the Chukchi and Beaufort Seas of the Arctic Ocean, and the Pacific Ocean lies to the south and southwest.

Alaska is the largest U.S. state by area, comprising more total area than the next three largest states of Texas, California, and Montana combined, and is the seventh-largest subnational division in the world. It is the third-least populous and most sparsely populated U.S. state, but with a population of 736,081 as of 2020, is the continent's most populous territory located mostly north of the 60th parallel, with more than quadruple the combined populations of Northern Canada and Greenland.[3] The state capital of Juneau is the second-largest city in the United States by area, and the former capital of Alaska, Sitka, is the largest U.S. city by area. Approximately half of Alaska's residents live within the Anchorage metropolitan area.

Indigenous people have lived in Alaska for thousands of years, and it is widely believed that the region served as the entry point for the initial settlement of North America by way of the Bering land bridge. The Russian Empire was the first to actively colonize the area beginning in the 18th century, eventually establishing Russian America, which spanned most of the current state, and promoted and maintained a native Alaskan Creole population.[4] The expense and logistical difficulty of maintaining this distant possession prompted its sale to the U.S. in 1867 for US$7.2 million (equivalent to $140 million in 2021). The area went through several administrative changes before becoming organized as a territory on May 11, 1912. It was admitted as the 49th state of the U.S. on January 3, 1959.[5]

Abundant natural resources have enabled Alaska—with one of the smallest state economies—to have one of the highest per capita incomes, with commercial fishing, and the extraction of natural gas and oil, dominating Alaska's economy. U.S. Armed Forces bases and tourism also contribute to the economy; more than half the state is federally-owned land containing national forests, national parks, and wildlife refuges.

The Indigenous population of Alaska is proportionally the highest of any U.S. state, at over 15 percent.[6] Various Indigenous languages are spoken, and Alaskan Natives are influential in local and state politics.

Summary:
```

### 21. Data Extraction Prompts

```
Extract the food items from the restaurant review below

Desired format: JSON array of food names

Input:
Was in the area and luckily spotted this gem, loved it. Good size seating area and some interesting options on the menu. We had the soup and the okonomiyaki. The portion size of the okonomiyaki was decent, doesn’t look that big in the picture but it was definitely enough for one. Would come here again.
```

### 22. Sentiment Analysis Prompts

```
Classify the following text's sentiment in one word among positive, neutral, or negative

Input:

Food was average at best. Breakfast burrito had an abundance of ingredients with total lack of flavour. Japanese pancake was okay but not great.  Coffee was bitter and uninspiring. Overall, wouldn't return. 1 star.

Output:
```

```
Classify the following text's sentiment

Desired format in a number: -1 for negative, 0 for neutral, and 1 for positive

Input:

Nice cafe with a good range of options. I found the staff to be friendly and polite. The cafe itself is clean, spacious and really nice in gwneral. The chai was very very nice with a great addition of honey on the side which not many places offer. The brioche bun was really tasty but the bacon was super dry and thin. I think this bun could be taken to the next level with a good, not overly cooked, piece of bacon. Thanks for the quick service today.

Output:
```

</details>
