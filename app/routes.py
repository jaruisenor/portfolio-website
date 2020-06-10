from flask import Flask, jsonify, session, render_template, request, Response, redirect, send_from_directory
from app import app
import os



@app.route("/", methods=['POST', 'GET'])
@app.route("/index", methods=['POST', 'GET'])
def index():
    Texto = "I’m an engineer undergraduate (soon to be graduate) with a back ground in mining and industrial engineering. I’m always looking to solve real world problems with an analytical perspective with data analytics, machine learning and data visualization tools at hand. The mix between business oriented formation and Data Analytics technical skills, I believe, makes a difference in todays world. This portfolio contains personal projects done in my leisure time involving Data Science."
    return render_template('index.html', title_text=Texto, title="DATA SCIENCE & WEB DEVELOPMENT", id="index")


