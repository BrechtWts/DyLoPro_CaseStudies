# __DyLoPro: Profiling the Dynamics of Event Logs - *Case Studies*__ 

This repository contains a beta version of the [DyLoPro package](#1-dylopro-package-beta) on the one hand, and [annotated notebooks](#2-extensive-case-studies-public-event-logs) with an extensive and comprehensive analysis of the dynamics over time for multiple public event logs commonly used in Process Mining literature, on the other hand. 

## __1. DyLoPro package (Beta)__
The __DyLoPro Python Library__ is a tool that allows PM practitioners to efficiently and comprehensively explore the dynamics in event logs over time, prior to applying PM techniques. These comprehensive exploration capabilities are provided by extensive set of plotting functionalities, visualizing the dynamics over time from different process perspectives. This repository includes a __beta__ version of the DyLoPro package, which will __soon__ be __launched publically__.

_"DyLoPro is a comprehensive visual analytics framework designed to explore event log dynamics over time. DyLoPro’s comprehensiveness is achieved through the incorporation of the main process perspectives - the control-flow, data (including resources) and performance, along two orthogonal dimensions of log concepts and representation types. It incorporates six log concepts to capture all essential information from event logs, including variants and directly-follows relations for the control-flow perspective, and categorical and numeric case and event features for the data perspective. These six log concepts can be represented using five representation types, including four performance-oriented ones (throughput time, number of events per case, outcome, and directly-follows-relations’ performance) and one generic type. With this two-dimensional approach, end users can gain a nuanced and holistic view of event log dynamics, efficiently identifying patterns, temporary or permanent changes, and trends of interest from multiple perspectives. Upon identification, they can further analyze these patterns and trends, ultimately leading to more appropriate application of downstream process mining techniques."_

How to use and access DyLoPro's variety of plotting methods in an efficient and unified manner, is demonstrated in the case studies' associated notebooks. Further information can be found in the documentation provided with each of the plotting methods. 

All of __DyLoPro__'s plotting methods construct time series by deriving real-valued measures for a choronologically ordered set of sublogs. This chronologically ordered set of sublogs is constructed by: 
1. Defining the `frequency` parameter, that determines the frequency by which the observations are grouped. E.g. here, for all visualizations, we use the default `frequency='weekly'`. As such, the time period covered by the entire event log is subdivided into a chronologically ordered set of weekly time intervals. 
1. Defining the `case_assignment` parameter, that determines the condition upon which each case is assigned to one of these equal-length time intervals. E.g. here, for all visualizations, we use the default `case_assignment='first_event'`. As such, each case is assigned to the time interval in which it first event occurs.

Consequently, e.g. for the BPIC19 case study with `frequency='weekly'` and `case_assignment='first_event'`, each case is assigned to the 1-week time interval in which its first event occurs and hence each sublog will consist of all cases that were initialized in one particular week. 


## __2. Extensive case studies public event logs__ 

Case studies are conducted for a number of commonly used public event logs. The associated annotated notebooks are: 

1. __BPIC_19.ipynb__: Comprehensive case study on the dynamics over time in the BPIC19 event log. The data can be found [here](https://doi.org/10.4121/uuid:d06aff4b-79f0-45e6-8ec8-e19730c248f1).
1. __BPIC_17.ipynb__: Comprehensive case study on the dynamics over time in the BPIC17 event log. The data can be found [here](https://doi.org/10.4121/uuid:5f3067df-f10b-45da-b98b-86ae4c7a310b).
1. Road_Traffic.ipynb: ...


