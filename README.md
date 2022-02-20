[![Python application test with Github Actions](https://github.com/noahgift/or/actions/workflows/main.yml/badge.svg)](https://github.com/noahgift/or/actions/workflows/main.yml)

## Operations Research

https://github.com/DEAP/deap

Operations Research Algorithms

The genesis of this code is from an Operations Research course at the UC Davis MBA program with Dr.David L Woodruff:  
http://faculty.gsm.ucdavis.edu/~dlw/

### To run container
`docker build -t fastapi:latest .`
`docker run -p 127.0.0.1:8080:8080 fastapi:latest`

A.  Then push to ECR

B.  Deploy via AWS App Runner




### Randomized Start with Greedy Path Solution for TSP

You can see a solution here:  https://github.com/noahgift/or/blob/master/greedy-random-tsp.py

```bash
(.venv) codespace ➜ ~/workspace/or (master ✗) $ ./greedy-random-tsp.py 10
Running simulation 10 times
Shortest Distance: 129
Optimal Route: [(b'URS', b'WFC', 0), (b'WFC', b'GPS', 1), (b'GPS', b'PCG', 1), (b'PCG', b'MCK', 3), (b'MCK', b'SFO', 16), (b'SFO', b'ORCL', 20), (b'ORCL', b'HPQ', 12), (b'HPQ', b'GOOG', 6), (b'GOOG', b'AAPL', 11), (b'AAPL', b'INTC', 8), (b'INTC', b'CSCO', 6), (b'CSCO', b'EBAY', 0), (b'EBAY', b'SWY', 32), (b'SWY', b'CVX', 13)]
(.venv) codespace ➜ ~/workspace/or (master ✗) $ 
```

![tsp](https://user-images.githubusercontent.com/58792/122964410-3df3c980-d355-11eb-9c03-ab101dfcd532.png)

### Examples of greedy algorithms and random choices

* [Colab Notebook on Greedy Algorithms and random choices](https://github.com/noahgift/or/blob/master/Explore_Greedy_Solutions.ipynb)
* [GCP Flask application serving our "greedy coin choices"](https://github.com/noahgift/or/blob/master/main.py)

### YouTube Series on Business Analytics

* [YouTube Business Analytics Lectures](https://www.youtube.com/watch?v=WnER8NU_UZs&list=PLdfopzFjkPz-2nmMKWaEvgEJjbfrtAOzb)
* [YouTube Containerize Algorithms to AWS](https://www.youtube.com/watch?v=SWAqetwqPiU) and on O'Reilly-Watch on O'Reilly Media: https://learning.oreilly.com/videos/learn-to-containerize/02202022VIDEOPAIML/

