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

Most Process Mining techniques assume that the underlying process and hence the data generating function of the associated event log is in a steady-state. However, in reality, this is rarily the case. 
>_"Applying PM on event logs in which this stationarity assumption does not hold, i.e. in which one or more drifts occur in the underlying process, can induce a significant yet oftentimes unnoticed bias in the results, leading to incorrect insights."_

New PM techniques proposed in the literature are frequently evaluated and compared using commonly employed public event logs. However, potential *sources of bias* stemming from underlying *event log drifts* are almost always overlooked. Therefore, case studies are conducted for a number of these commonly used public event logs. They demonstrate both the usefulness and effectiveness of leveraging the DyLoPro framework and library for comprehensively analyzing the dynamics over time from multiple perspectives. Each case study is documented in an annotated notebook that uncovers the most interesting trends / patterns and changes over time for the associated event logs. 

These case studies significantly enhances the transparency of several public event logs widely employed in the Process Mining literature, thereby contributing to the advances in the field of PM in several ways: 
1. Enabling Process Mining researchers to interpret the results of their proposed techniques when applied on these logs in a more informed manner. 
1. The differences in results between techniques can be identified with a better understanding of potential sources of bias.
1. Enabling researchers to make more informed decisions on how to preprocess the event logs and take appropriate actions to address any patterns or drifts that may induce bias in the results.
1. Assisting researchers in potentially even determining how to subset the data to avoid bias.

The overall advantages of the increased transparency provided by these case studies, and hence provided by the __DyLoPro package__ in general, demonstrate its potential to significantly improve the quality and accuracy of Process Mining research and contribute to advancing the field.

>_"The impact of drifts in different perspectives on the results of the process mining techniques varies depending on the technique used."_

The primary aim of __DyLoPro__ is not to provide a conclusive answer on the root causes and consequences of certain drifts, but rather to enable researchers and practitioners to efficiently explore a wide range of dynamics present in the often very complex data structures that event logs are, and accordingly efficiently identify any changes, trends or patterns of interest for subsequent analysis. Researchers might or might not decide to further analyze certain identifed drifts or patterns, depending on the Process Mining task at hand. 

The associated annotated notebooks are: 

1. __BPIC_19.ipynb__: Comprehensive case study on the dynamics over time in the BPIC19 event log. The data can be found [here](https://doi.org/10.4121/uuid:d06aff4b-79f0-45e6-8ec8-e19730c248f1).
1. __BPIC_17.ipynb__: Comprehensive case study on the dynamics over time in the BPIC17 event log. The data can be found [here](https://doi.org/10.4121/uuid:5f3067df-f10b-45da-b98b-86ae4c7a310b).
1. __BPIC_15.ipynb__: Comprehensive case study on the dynamics over time in the BPIC15 event log. The data can be found [here](https://doi.org/10.4121/uuid:31a308ef-c844-48da-948c-305d167a0ec1). __COMING SOON...__
1. __BPIC_12.ipynb__: Comprehensive case study on the dynamics over time in the BPIC12 event log. The data can be found [here](https://doi.org/10.4121/uuid:3926db30-f712-4394-aebc-75976070e91f). __COMING SOON...__
1. __BPIC_20__: BPIC_20 event log is a collection of 5 event logs pertaining to the travel administration at a university. Each event log covers the cases of a different process. An overview of the data can be found [here](https://doi.org/10.4121/uuid:52fb97d4-4588-43c9-9d04-3604d4613b51).
    1. __BPIC_20_DomDecl.ipynb__: Comprehensive case study on the dynamics over time in the __Domestic Declaration__ event log. The data can be found [here](https://doi.org/10.4121/uuid:3f422315-ed9d-4882-891f-e180b5b4feb5). __COMING SOON...__
    1. __BPIC_20_IntlDecl.ipynb__: Comprehensive case study on the dynamics over time in the __International Declaration__ event log. The data can be found [here](https://doi.org/10.4121/uuid:2bbf8f6a-fc50-48eb-aa9e-c4ea5ef7e8c5). __COMING SOON...__
    1. __BPIC_20_PpTravel.ipynb__: Comprehensive case study on the dynamics over time in the __Prepaid Travel Costs__ event log. The data can be found [here](https://doi.org/10.4121/uuid:5d2fe5e1-f91f-4a3b-ad9b-9e4126870165). __COMING SOON...__
    1. __BPIC_20_TravelPermit.ipynb__: Comprehensive case study on the dynamics over time in the __Travel Permit Data__ event log. The data can be found [here](https://doi.org/10.4121/uuid:ea03d361-a7cd-4f5e-83d8-5fbdf0362550). __COMING SOON...__
    1. __BPIC_20_RequestPay.ipynb__: Comprehensive case study on the dynamics over time in the __Request For Payment__ event log. The data can be found [here](https://doi.org/10.4121/uuid:895b26fb-6f25-46eb-9e48-0dca26fcd030). __COMING SOON...__
1. __Road_Traffic.ipynb__: Comprehensive case study on the dynamics over time in the __Road Traffic Fines Management__ event log. The data can be found [here](https://doi.org/10.4121/uuid:270fd440-1057-4fb9-89a9-b699b47990f5). __COMING SOON...__
1. __Hospital_Billing.ipynb__: Comprehensive case study on the dynamics over time in the __Hospital Billing__ event log. The data can be found [here](https://doi.org/10.4121/uuid:76c46b83-c930-4798-a1c9-4be94dfeb741). __COMING SOON...__
