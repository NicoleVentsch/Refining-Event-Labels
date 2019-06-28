# Refining-Event-Labels

## Use Case

Many processes involve carrying out an action multiple times. An example for this would be an online shop in which you first have to pay a registration fee before ordering an item and paying it. This process contains the event “payment" twice, but in different contexts, so that the payments are actually two different tasks. In the context of analysing processes, the event logs usually only contain the event names, so that the “payment" actions would be treated as the same task and loops would be induced in the resulting models. However, these loops do not match the actual process, which is the issue this project addresses. 

These imprecise logs should be refined based on the structural contexts of the events. We want to refine the logs without any filtering. Moreover, we want to allow an interactive change of the thresholds used to refine the labels since this can vary for each log and we lack knowledge on the correctness of the refined log in general. All of this should be done by implementing an algorithm in Python and then creating a web service through which the user can modify his event log. The algorithm used for this task is based on the paper “Handling duplicated tasks in process discovery by refining event labels” by Xixi Lu et al. 


## System Overview

The “Refining Labels” system is a web-based application that allows for relabelling of event logs based on the algorithm proposed in the paper of Xixi Lu et al. It provides all the functionalities required to carry out the refinement by relabelling events differently based on their behaviours (context in the event log). 
The foundation of the system is based on the following features:
- A flexible method to upload event log files in either XES or CSV format.
- An interactive way to adjust the thresholds required for the algorithm.
- An interactive way to select the candidate labels (namely, “imprecise labels”).
-  A flexible method to download the refined event log in XES format.
As the optimal refined event log or model may be unknown, the system provides the user with the freedom to manipulate the thresholds and candidate labels and finally chose the event log which is considered to be the best one (according to user’s expertise).


## The assumptions

In this project we will assume that an event log is given by the user, i.e., data that contains at least the attributes "id", "time stamp" and "activity name". Furthermore, we will assume that these event logs are given in the standard XES format. Since the set of candidates for imprecise labels is given by the user, we assume that the quality of the processes applied on the refined event log also depends on the domain knowledge of the user who picks the candidate labels.
The algorithm is a pre-processing step itself and it does not include other pre-processing mechanisms like filtering.
In this context, instead of considering imprecise labels as noise and filtering them out, we change the labels based on the patterns present in the data.


## Supporting Tools

We make use of the following open source tools (for further details and documentation, see references): 
- [Python 3.7.2 as back-end programming language](https://docs.python.org/3/)
- [pm4py, Python library as process mining toolkit](http://pm4py.org/)
- [NetworkX, Pyhton library for graph manipulation](https://networkx.github.io/documentation/networkx-2.2/)
- [Flask 1.0.2 as web application framework 2 Project](http://flask.pocoo.org/docs/1.0/)
- [JavaScript as front-end development language (Standard ECMAScript 2018)](https://www.ecma-international.org/ecma-262/9.0/index.html)


