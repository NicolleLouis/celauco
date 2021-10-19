# Covid Simulator

--- 

## Installation

```bash
pip install -r requirements.txt
```

## Usage

There is 3 way to run this project:
- Visualization (Display the model and agents in a real time grid):
  - Update `script_visualize.py` with options you want
  - Run `make visualize`
- Clean graph, 1 run:
  - Update `script_plot.py` with Celauco Models parameters adapted, also change graph_title
  - Run `make plot`
  - Look at results inside directory: `graph/single`
- Graph for batch run:
  - Update `script_batch.py` with Celauco Models parameters adapted, also change run_number and graph title
  - Run `make batch`
  - Look at results inside directory: `graph/batch`

---

## Troubleshooting

If you encounter a bug or an abnormal behaviour, open a github issue and try to explain as precisely as possible your issue

---

## Participate in the project

- I have an idea but no time to code:
  - Open an issue on github explaining your idea and why it's great. Try to be precise

- I have an idea and a PullRequest:
  - Open the Pull Request and explain its goal. I'll review it as fast as possible

- I'm a developer, I want to help the project:
  - Easiest way is to contact me directly (louis.a.nicolle@gmail.com)
  - Some project ideas are listed [here](IDEAS.md)