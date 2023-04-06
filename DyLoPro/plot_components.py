# import pandas as pd
# import numpy as np
# import datetime as dt
# import matplotlib.pyplot as plt 

def plt_period_tt(x, y, axes, time_unit, numeric_agg, location= 'right', color='red', shared=False):
    '''
        args:
            - x:            data horizontal axis ; periodic timestamps
            - y:            data vertical axis 
            - axes:           matplotlib.axes.Axes object; the axis on which the periodic numeric_agg of the throughput time needs to be plotted
            - time_unit:    string = 'seconds', 'minutes', 'hours' or 'days' (default) ; time unit for Throughput Time 
            - numeric_agg:  string = 'mean' (default) or 'median' ; numeric aggregation of the periodic TT
            - location:     string = 'left', 'right' (default) or 'only' (no twinx on same plot); indicating whether the periodic evolution of the amount
                            of cases initialized is plotted on the main left axis, the twin right axis, or whether there are no twin axes on this particular plot. 
            - color:        string ; 'red' by default ; color of the line plot. 
            - shared:       boolean = False (default) ; setting shared to True only useful when location='only', and needed when this axes is shared by multiple graphs. 
        plots: evolution of the periodic numeric_agg of the Throughput Time.
    '''
    if location=='left': 
        axes.plot(x, y, label="{} Throughput Time ({})".format(numeric_agg, time_unit), color= color,marker='o')
        axes.legend(loc='upper left')
        axes.grid(True, axis='x')
        axes.set_ylabel("{} Throughput Time".format(numeric_agg), color=color)
    elif location=='right':
        axes.plot(x, y, label="{} Throughput Time ({})".format(numeric_agg, time_unit), color= color,marker='o')
        axes.legend(loc='upper right')
        axes.set_ylabel("{} Throughput Time".format(numeric_agg), color=color)
    elif location=='only':
        if shared:
            axes.plot(x, y, label="{} Throughput Time ({})".format(numeric_agg, time_unit),marker='o')
        else:
            axes.plot(x, y,marker='o')
        axes.grid(True)
        axes.set_ylabel("{} Throughput Time".format(numeric_agg))

def plt_period_caseinits(x, y, axes, location= 'left', color='blue', shared=False):
    '''
        args:
            - x:            data horizontal axis ; periodic timestamps
            - y:            data vertical axis 
            - axes:         matplotlib.axes.Axes object; the axis on which the periodic numeric_agg of the throughput time needs to be plotted
            - numeric_agg:  string = 'mean' (default) or 'median' ; numeric aggregation of the periodic TT
            - location:     string = 'left', 'right' (default) or 'only' (no twinx on same plot); indicating whether the periodic numeric_agg of Throughput
                            Time (tt) is plotted on the main left axis, the twin right axis, or whether there are no twin axes on this particular plot. 
            - color:        string ; 'red' by default ; color of the line plot. 
            - shared:       boolean = False (default) ; setting shared to True only useful when location='only', and needed when this axes is shared by multiple graphs. 
        plots: evolution of the periodic numeric_agg of the Throughput Time.
    '''
    if location=='left': 
        axes.plot(x, y, label="# cases initialized", color = color, marker='o')
        axes.legend(loc='upper left')
        axes.grid(True, axis='x')
        axes.set_ylabel("# Cases", color=color)
    elif location=='right':
        axes.plot(x, y, label="# cases initialized", color = color, marker='o')
        axes.legend(loc='upper right')
        axes.set_ylabel("# Cases", color=color)
    elif location=='only':
        if shared:
            axes.plot(x, y, label="# cases initialized", marker='o')
            axes.legend()
        else:
            axes.plot(x, y, marker='o')
        axes.grid(True)
        axes.set_ylabel("# Cases")
    
def plt_period_dfrpercase(x, y, axes, number, dfr_string, frequency, max_k, location='only', color='blue', shared=False):
    '''
        args:
            - x:            data horizontal axis ; periodic timestamps
            - y:            data vertical axis 
            - axes:         matplotlib.axes.Axes object; the axis on which the periodic numeric_agg of the throughput time needs to be plotted
            - number:       int; number i of the Directly-Follows Relation (dfr) with dfr i being the i'th most frequently occurring dfr. 
            - dfr_string:   string; name of the directly follows relationship. 
            - frequency:    string = 'daily', 'weekly' (default), 'two weekly' or 'monthly' ; frequency by which the observations are
                            grouped together.
            - max_k:        int ; only the max_k most frequently occurring Directly-Follows Relations are plotted.
            - location:     string = 'left', 'right' (default) or 'only' (no twinx on same plot); indicating whether the periodic DFR ratio is
                            plotted on the main left axis, the twin right axis, or whether there are no twin axes on this particular plot. 
            - color:        string ; 'blue' by default ; color of the line plot. 
            - shared:       boolean = False (default) ; setting shared to True only useful when location='only', and needed when this axes is shared by multiple graphs. 
        plots: univariate evolution of the periodic #DFR / cases.
    '''
    if location=='left': 
        axes.plot(x, y, label="DFR {}. {}".format(number, dfr_string), color = color, marker='o')
        axes.legend(loc='upper left')
        axes.grid(True, axis='x')
        axes.set_ylabel("[#{}]/case".format(dfr_string), color=color)
    elif location=='right':
        axes.plot(x, y, label="DFR {}. {}".format(number, dfr_string), color = color, marker='o')
        axes.legend(loc='upper right')
        axes.set_ylabel("[#{}]/case".format(dfr_string), color=color)
    elif location=='only':
        if shared:
            axes.plot(x, y, label="DFR {}. {}".format(number, dfr_string), marker='o')
            if number==max_k:
                axes.legend(loc="upper left", fontsize='x-small')
                axes.set_ylabel("# Directly-Follows Relations (DFR) per Case")
                axes.grid(True)
                axes.set_title("{} evolution of #occurances/case for the {} most common Direclty-Follows Relationships (DFRs)".format(frequency, max_k))
        else:
            axes.plot(x, y, marker='o')
            axes.set_ylabel("[#{}]/case".format(dfr_string))
            axes.set_title("DFR {}. {}:{} evolution of #occurances/case".format(number, dfr_string, frequency))
            axes.grid(True)
#Adjusted: 
def plt_period_dfrpercase(x, y, axes, number, frequency, max_k, location='only', color='blue', shared=False):
    '''
        args:
            - x:            data horizontal axis ; periodic timestamps
            - y:            data vertical axis 
            - axes:         matplotlib.axes.Axes object; the axis on which the periodic numeric_agg of the throughput time needs to be plotted
            - number:       int; number i of the Directly-Follows Relation (dfr) with dfr i being the i'th most frequently occurring dfr. 
            - frequency:    string = 'daily', 'weekly' (default), 'two weekly' or 'monthly' ; frequency by which the observations are
                            grouped together.
            - max_k:        int ; only the max_k most frequently occurring Directly-Follows Relations are plotted.
            - location:     string = 'left', 'right' (default) or 'only' (no twinx on same plot); indicating whether the periodic DFR ratio is
                            plotted on the main left axis, the twin right axis, or whether there are no twin axes on this particular plot. 
            - color:        string ; 'blue' by default ; color of the line plot. 
            - shared:       boolean = False (default) ; setting shared to True only useful when location='only', and needed when this axes is shared by multiple graphs. 
        plots: univariate evolution of the periodic #DFR / cases.
    '''
    if location=='left': 
        axes.plot(x, y, label="DFR {}".format(number), color = color, marker='o')
        axes.legend(loc='upper left')
        axes.grid(True, axis='x')
        axes.set_ylabel("Number of DFR {} per case".format(number), color=color)
    elif location=='right':
        axes.plot(x, y, label="DFR {}".format(number), color = color, marker='o')
        axes.legend(loc='upper right')
        axes.set_ylabel("Number of DFR {} per case".format(number), color=color)
    elif location=='only':
        if shared:
            axes.plot(x, y, label="DFR {}".format(number), marker='o')
            if number==max_k:
                axes.legend(loc="upper left", fontsize='x-small')
                axes.set_ylabel("# Directly-Follows Relations (DFR) per Case")
                axes.grid(True)
                axes.set_title("{} evolution of #occurances/case for the {} most common Direclty-Follows Relationships (DFRs)".format(frequency, max_k))
        else:
            axes.plot(x, y, marker='o')
            axes.set_ylabel("Number of DFR {} per case".format(number))
            axes.set_title("DFR {}: {} evolution of #occurances/case".format(number, frequency))
            axes.grid(True)

#General categorical plotting function: 
#Adjusted: 
#So firrst adjust dfr references that they do not give the string of the dfr anymore. Then transform it so that they can use this one. Also for variants. 
def plt_period_nominal(x, y, axes, y_label, number=None, max_k=None, title=None, label=None,  location=None, color=None):
    '''
        Generic plotting function for categoricals. 4 options:
            1.  Data needs to be plotted on a figure with 1 other plot, with each of the 2 plots a different vertical axis (left and right). This data is assigned to the 
                left vertical axis. Needed arguments: the required arguments, label = string, location = 'left', color = string.
            2.  Data needs to be plotted on a figure with 1 other plot, with each of the 2 plots a different vertical axis (left and right). This data is assigned to the 
                right vertical axis. Needed arguments: the required arguments, label = string, location = 'right', color = string.
            3.  Data needs to be plotted on a figure that will not contain any other plots. Needed arguments: the required arguments, title = string. 
            4.  Data needs to be plotted on a figure that will contain several other plots, but all of the same quantity / unit. Hence, only one vertical axis (the left one)
                will be used by max_k plots. Needed arguments: the required arguments, number = int, max_k = int, title = string, label = string.
        args:
            - x:            data horizontal axis ; periodic timestamps
            - y:            data vertical axis 
            - axes:         matplotlib.axes.Axes object; the axis on which the periodic numeric_agg of the throughput time needs to be plotted
            - y_label:      string ; y_label that describes the data on the vertical axis.
            - number:       int; None by default, only needed for plotting option 4.
            - max_k:        int ; None by default, only needed for plotting option 4. 
            - title:        string; None by default, only needed for plotting options 3 & 4.
            - label:        string; None by default, only needed for plotting option 1, 2 & 4.
            - location:     string; None by default, only needed for plotting option 1 (= 'left) & 2 (='right'). 
            - color:        string; None by default, only needed for plotting option 1 & 2. 
        plots: univariate evolution of the periodic #DFR / cases.
    '''
    if color:
        if location=='left': #1
            # axes.plot(x, y, label="DFR {}".format(number), color = color, marker='o')
            axes.plot(x, y, label=label, color = color, marker='o')
            axes.legend(loc='upper left')
            axes.grid(True, axis='x')
            # axes.set_ylabel("Number of DFR {} per case".format(number), color=color)
            axes.set_ylabel(y_label, color=color)
        elif location=='right': #2
            # axes.plot(x, y, label="DFR {}".format(number), color = color, marker='o')
            axes.plot(x, y, label=label, color = color, marker='o')
            axes.legend(loc='upper right')
            # axes.set_ylabel("Number of DFR {} per case".format(number), color=color)
            axes.set_ylabel(y_label, color=color)

    else:
        if label: #4
            # axes.plot(x, y, label="DFR {}".format(number), marker='o')
            axes.plot(x, y, label=label, marker='o')
            if number==max_k:
                axes.legend(loc="upper left", fontsize='x-small')
                # axes.set_ylabel("# Directly-Follows Relations (DFR) per Case")
                axes.set_ylabel(y_label)
                axes.grid(True)
                # axes.set_title("{} evolution of #occurances/case for the {} most common Direclty-Follows Relationships (DFRs)".format(frequency, max_k))
                axes.set_title(title)
        else: #3
            axes.plot(x, y, marker='o')
            # axes.set_ylabel("Number of DFR {} per case".format(number))
            axes.set_ylabel(y_label)
            axes.grid(True)
            # axes.set_title("DFR {}: {} evolution of #occurances/case".format(number, frequency))
            axes.set_title(title)


    # if location=='left': 
    #     axes.plot(x, y, label="DFR {}".format(number), color = color, marker='o')
    #     axes.legend(loc='upper left')
    #     axes.grid(True, axis='x')
    #     axes.set_ylabel("Number of DFR {} per case".format(number), color=color)
    # elif location=='right':
    #     axes.plot(x, y, label="DFR {}".format(number), color = color, marker='o')
    #     axes.legend(loc='upper right')
    #     axes.set_ylabel("Number of DFR {} per case".format(number), color=color)
    # elif location=='only':
    #     if shared:
    #         axes.plot(x, y, label="DFR {}".format(number), marker='o')
    #         if number==max_k:
    #             axes.legend(loc="upper left", fontsize='x-small')
    #             axes.set_ylabel("# Directly-Follows Relations (DFR) per Case")
    #             axes.grid(True)
    #             axes.set_title("{} evolution of #occurances/case for the {} most common Direclty-Follows Relationships (DFRs)".format(frequency, max_k))
    #     else:
    #         axes.plot(x, y, marker='o')
    #         axes.set_ylabel("Number of DFR {} per case".format(number))
    #         axes.set_title("DFR {}: {} evolution of #occurances/case".format(number, frequency))
    #         axes.grid(True)
#General plotting function that could be used for everything. 
def plt_period(x, y, axes, y_label, number=None, max_k=None, title=None, label=None,  location=None, color=None):
    '''
        Generic plotting function. 4 options:
            1.  Data needs to be plotted on a figure with 1 other plot, with each of the 2 plots a different vertical axis (left and right). This data is assigned to the 
                left vertical axis. Needed arguments: the required arguments, label = string, location = 'left', color = string.
            2.  Data needs to be plotted on a figure with 1 other plot, with each of the 2 plots a different vertical axis (left and right). This data is assigned to the 
                right vertical axis. Needed arguments: the required arguments, label = string, location = 'right', color = string.
            3.  Data needs to be plotted on a figure that will not contain any other plots. Needed arguments: the required arguments, title = string. 
            4.  Data needs to be plotted on a figure that will contain several other plots, but all of the same quantity / unit. Hence, only one vertical axis (the left one)
                will be used by max_k plots. Needed arguments: the required arguments, number = int, max_k = int, title = string, label = string.
        args:
            - x:            data horizontal axis ; periodic timestamps
            - y:            data vertical axis 
            - axes:         matplotlib.axes.Axes object; the axis on which the periodic numeric_agg of the throughput time needs to be plotted
            - y_label:      string ; y_label that describes the data on the vertical axis.
            - number:       int; None by default, only needed for plotting option 4.
            - max_k:        int ; None by default, only needed for plotting option 4. 
            - title:        string; None by default, only needed for plotting options 3 & 4.
            - label:        string; None by default, only needed for plotting option 1, 2 & 4.
            - location:     string; None by default, only needed for plotting option 1 (= 'left) & 2 (='right'). 
            - color:        string; None by default, only needed for plotting option 1 & 2. 
    '''
    marker_list = ['o', 's', '+', 'x', 'D', 'P', '1', 'v', '*', '>', '<']
    num_markers = len(marker_list)
    
    if color:
        if location=='left': #1
            axes.plot(x, y, label=label, color = color, marker='o')
            axes.legend(loc='upper left')
            axes.grid(True, axis='x')
            axes.set_ylabel(y_label, color=color)
        elif location=='right': #2
            # axes.plot(x, y, label="DFR {}".format(number), color = color, marker='o')
            axes.plot(x, y, label=label, color = color, marker='s')
            axes.legend(loc='upper right')
            # axes.set_ylabel("Number of DFR {} per case".format(number), color=color)
            axes.set_ylabel(y_label, color=color)
        if title:
            axes.set_title(title)

    else:
        if label: #4
            # Marker_idx configured st in case of number > num_markers, 
            # we start again at the beginning of the marker list. 
            marker_idx = number - 1 - num_markers*((number-1)//num_markers)
            axes.plot(x, y, label=label, marker= marker_list[marker_idx])
            if number==max_k:
                if max_k > 2: 
                    axes.legend(loc="upper left", fontsize='x-small')
                else:
                    axes.legend()
                # axes.set_ylabel("# Directly-Follows Relations (DFR) per Case")
                axes.set_ylabel(y_label)
                axes.grid(True)
                # axes.set_title("{} evolution of #occurances/case for the {} most common Direclty-Follows Relationships (DFRs)".format(frequency, max_k))
                axes.set_title(title)
        else: #3
            axes.plot(x, y, marker='o')
            # axes.set_ylabel("Number of DFR {} per case".format(number))
            axes.set_ylabel(y_label)
            axes.grid(True)
            # axes.set_title("DFR {}: {} evolution of #occurances/case".format(number, frequency))
            axes.set_title(title)




def plt_period_variant_prc(x, y, axes, var_num, frequency, max_k, location='only', color='blue', shared=False):
    '''
        args:
            - x:            data horizontal axis ; periodic timestamps
            - y:            data vertical axis 
            - axes:         matplotlib.axes.Axes object; the axis on which the periodic numeric_agg of the throughput time needs to be plotted
            - var_num:       int; number i of the variant with variant i being the i'th most frequently occurring variant. 
            - frequency:    string = 'daily', 'weekly' (default), 'two weekly' or 'monthly' ; frequency by which the observations are
                            grouped together.
            - max_k:        int ; only the max_k most frequently occurring Directly-Follows Relations are plotted.
            - location:     string = 'left', 'right' (default) or 'only' (no twinx on same plot); indicating whether the periodic DFR ratio is
                            plotted on the main left axis, the twin right axis, or whether there are no twin axes on this particular plot. 
            - color:        string ; 'blue' by default ; color of the line plot. 
            - shared:       boolean = False (default) ; setting shared to True only useful when location='only', and needed when this axes is shared by multiple graphs. 
        plots: univariate evolution of the periodic percentage of cases accounted for by variant var_num.
    '''
    if location=='left': 
        axes.plot(x, y, label="Variant {}".format(var_num), color = color, marker='o')
        axes.legend(loc='upper left')
        axes.grid(True, axis='x')
        axes.set_ylabel("Variant {}: % cases".format(var_num), color = color)
    elif location=='right':
        axes.plot(x, y, label="Variant {}".format(var_num), color = color, marker='o')
        axes.legend(loc='upper right')
        axes.set_ylabel("Variant {}: % cases".format(var_num), color = color)
    elif location=='only':
        if shared:
            axes.plot(x, y, label="Variant {}".format(var_num), marker='o')
            if var_num==max_k:
                axes.legend(loc="upper left", fontsize='x-small')
                axes.set_ylabel("Fraction of initialized cases")
                axes.grid(True)
                axes.set_title("{} evolution fraction of initialized cases belonging to the {} most common variants".format(frequency, max_k))
        else:
            axes.plot(x, y, marker='o')
            axes.set_ylabel("Variant {}: % cases".format(var_num))
            axes.set_title("Variant {}:{} evolution of fraction cases it accounts for".format(var_num, frequency))
            axes.grid(True)

