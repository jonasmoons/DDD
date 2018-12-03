#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:49:15 2018

@author: jorndekleine
"""
import pandas as pd


dataset_survey=pd.read_csv("survey_data.csv",delimiter=",")
dataset_steps=pd.read_csv("steps_data.csv",delimiter=";")


df = pd.merge(dataset_survey,dataset_steps, on="id")

df["waist"]


def values(x):
    if (x > 135):
        return float("NaN")
    if (x <40):
        return float("NaN")
    else: 
        return x

df['waist'] = df['waist'].apply(values)

df.plot(y='waist')
