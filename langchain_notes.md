# Working with langchain chains in AzureML

## Introduction

Langchain has been very popular in the recent months and the community has been growing rapidly. Here are some tips and trick on how to work with langchain chains in AzureML.

## Monkey Patching Langchain to improve logging

The first thing I did when I started to work with Langchain was to patch it to get more logging information. Langchain does a great job at abstracting away what is really going on under the hood, in particular when working with more complex chains or agents. However, this abstraction comes at the cost of not being able to see what is really going on.

Instead of patching the code, I could have also use a callback, but I found that monkey patching was easier to use since I didn't have to change the code I was running -- for instance, I could just run an off-the-shelf agent and get the logging information.

What my patch does is to add wrap some key functions that langchain uses and log the parameters that go into them and the value that is returned by them to MLFlow as an artifact.

## Example of an Agent



## The Task

The main task used here is a simple question answering task on AzureML. The user asks a question and the system answers it. In order to answer the question, the system needs to retrieve some context from a cognitive services search index which is then used to generate the answer. 




