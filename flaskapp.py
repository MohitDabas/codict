from flask import Flask,render_template,request,jsonify
app=Flask(__name__)
import requests
from pythonDoc import pythonsendSuggestion,pythonDescribeRequest
from phpDoc import phpsendSuggestion,phpDescribeRequest
from javascriptDoc import javascriptsendSuggestion,javascriptDescribeRequest
from javaDoc import javasendSuggestion,javaDescribeRequest
from nodejsDoc import nodejssendSuggestion,nodejsDescribeRequest


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getlangnfunc',methods=['GET','POST'])
def getLangFunc():
    language=request.form['langSelection']
    functionName=request.form['functionName']
    if len(functionName)==0:
        return jsonify([])
    if language=='Python':    
        return jsonify(pythonsendSuggestion(functionName))
    if language=='PHP':
        return jsonify(phpsendSuggestion(functionName))    
    if language=='Javascript':
        return jsonify(javascriptsendSuggestion(functionName))     
    if language=='Java':
        return jsonify(javasendSuggestion(functionName))
    if language=='NodeJs':
        return jsonify(nodejssendSuggestion(functionName))           

@app.route('/describe',methods=['GET'])
def describe():
     lang=request.args.get('language')
     functionName=request.args.get('functionName')
     pathName=request.args.get('path')
     if lang=='Python':
      return pythonDescribeRequest(functionName,pathName)
     if lang=='PHP':
        return phpDescribeRequest(functionName,pathName) 
     if lang=='Java':
         return javaDescribeRequest(functionName,pathName)
     if lang=='Javascript':
         return javascriptDescribeRequest(functionName,pathName)    
     if lang=='NodeJs':
         return nodejsDescribeRequest(functionName,pathName)    
    

@app.route('/codesearch',methods=['GET'])   
def codesearch():
    from gitSearch import codesearch
    lang=request.args.get('lang')
    functionName=request.args.get('function')
    print(lang,functionName)
    return gitSearch.codesearch(lang,functionName)

@app.route('/getcurlcommand',methods=['POST'])
def getCurlCommand():
     curlCommand=request.form['curlCommand']
     print (curlCommand)
     try:
         fO=open('curlCommand.txt','w')
         fO.write(curlCommand)
         fO.close()
         return jsonify({'Message':'CURL command  stored Successfully.You may close the box'}) 

     except:
         return jsonify({'Message':'CURL command not stored Error'})    
    



    




if __name__=="__main__":
      app.run(host='0.0.0.0',port=80,debug=True)