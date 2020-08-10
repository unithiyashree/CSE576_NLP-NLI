# NLP-NLI


Natural Language Inference

The task is to learn a textual entailment function that takes two sentences ‘premise’ and ‘hypothesis’ and decides whether the premise entails the hypothesis, contradicts the hypothesis or is neutral to the hypothesis.

Architecture:
premise_representaion = f(Premise)
hypothesis_representation = f(Hypothesis)
output = softmax(g(premise_representaion, hypothesis_representation))
