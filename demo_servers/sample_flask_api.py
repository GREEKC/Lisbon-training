from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
import subprocess
import json
import string

app = FlaskAPI(__name__)

methods = {
    "grep": "grep \"Nice\" *",
    "ls": "ls",
}


@app.route("/processes_available", methods=['GET'])
def processes_available():
    """
    List all possible process options
    """
    return [methods[idx] for idx in methods]


@app.route("/run/<string:process>/", methods=['GET','POST'])
def run_process(process):
    """
    Run a selection of shell process and report the output
    """

    if request.method == 'GET':
        shellCommand = methods.get(process)
        print 'User requests ' + shellCommand
        process = subprocess.Popen(
            shellCommand, shell=True, stdout=subprocess.PIPE
        )
        data = process.communicate()[0]
        data = consumeShellOutput(data)
        # Needs error checking on [1] of communicate output.
        return data, status.HTTP_200_OK
    elif request.method == 'POST':
        # return "Method not implemented", status.HTTP_501_NOT_IMPLEMENTED

        resultBuffer = []

        shellCommand = methods.get(process)
        clientJson = request.get_json()
        for path in clientJson['paths']:

            process = subprocess.Popen(
                [shellCommand,clientJson['option'],path], shell=False, stdout=subprocess.PIPE
            )
            
            data = process.communicate()[0]
            data = consumeShellOutput(data)
            resultBuffer.append(data)

        return data, status.HTTP_200_OK

def consumeShellOutput(data):
    """
    Unpacks text data and turns it into some kind of primitive JSON
    """
    niceData = string.split(data,"\n")
    processedData = json.dumps(niceData, indent=4, separators=(",",': '))
    return processedData

if __name__ == "__main__":
    app.run(debug=True)
