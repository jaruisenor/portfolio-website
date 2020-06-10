from flask import Flask, jsonify, session, render_template, request, Response, redirect, send_from_directory
from app import app
import os
from PIL import Image


@app.route("/", methods=['POST', 'GET'])
@app.route("/index", methods=['POST', 'GET'])
def index():
    
    return render_template('index.html', title_text='Titulo Temporal', title="DATA SCIENCE & SUSTAINABILITY", id="index")


