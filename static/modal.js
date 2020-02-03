//get the modal
function getCurlCommand(){
    curlCommand=document.getElementById('CurlCommand');
    //alert(curlCommand.value);
   
    $.ajax({
        url:'/getcurlcommand',
        type:'POST',
        data:{'curlCommand':curlCommand.value},
        success: function(result){
       
        
            alert(result['Message']);
        }

    });
    
}




function getClick(tabName) {

    var modal = document.getElementById("myModal");
    //Get the span element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    if (tabName === 'Codict') {
        modal.style.display = "block";
        textForModal = document.getElementById("abtTab");
        textForModal.innerHTML = `<h3>Intro:</h3><br/><span>Codict is a tool that I coded because I need Quick Code's snippets, relevant, methods, functions definitions and their usages without setting up a new programming environment or downloading and reading programming Language's documentation while Doing <b>SAST</b>.
        The framework can also be used for learning programming.</span><br/><br/>
        <span>The Codict's Interface Contains three different individual blocks the first one is for  searching functions,getting relevant cod snippets from Github Search</span><br/><br/>
        <span>Second block is for your code which your going to inspect and investigate.No need to open Code in editor just paste your code here and copy it directly to interpreter or compiler.</span><br/><br/>
        <span>The Third block is for <b>compiler</b> and the <b>interpreter</b> from <a href="https://repl.it/">Repl.it</a></span>`;
    }

    if (tabName === 'Credits') {
        modal.style.display = "block";
        textForModal = document.getElementById("abtTab");
        textForModal.innerHTML=`<h3>Credits:</h3><br/><span>All credit goes to <a href="https://devdocs.io/">devdocs.io</a> They have made a great collection of different programming language.I just copied their database.Another credit goes to <a href="https://repl.it/">Repl.it</a> for providing us different compilers and interpreters directly on the web</span><br/><br/>
        <span>On the last Node I just want to say I am just a mechanic who assembled these twofollow me on github,twitter</span>`

        }

    //CodeSearch
    if(tabName==='CodeSearch'){
        modal.style.display = "block";
        textForModal = document.getElementById("abtTab");
        textForModal.innerHTML=`<h3>Enable Github Code Search</h3><br/><span>Currently github Api doesn't provide API to directly search in the code you need to search it from web interface.In case you know how to do it please DM me @ <a href="https://twitter.com/DabasMonty">Mohit Dabas</a> </span><br/><br/>
        <span>For now you need to explicitly enter <b>copy as curl command</b> while browsing github.com with your acccount being logged in from Browser's Network Tab</span><br/><br/>
        <span>You can make <b>dummy account</b> with any temporary mail service or you can alse use your <b>own account</b> We don't record any session </span><br/><br/>
        <span>The whole process is defined below in pictures</span>
        <h4><u>1. Login with your github account</h4></u><br/>
        <img src="./static/loginwithgithub.png" width="900px">
        <h4><u>2. Open network tab after successful login and reload https://www.github.com </h4></u><br/>
        <img src="./static/networktab.png" width="900px">
        <h4><u>3. The request url must be https://github.com</h4></u><br/>
        <img src="./static/choosegithub.png" width="900px">
        <h4><u>4. Right click on the request then copy option 'copy as curl'  </h4></u><br/>
        <img src="./static/copyascurl.png" width="900px">
        <h4><u>5.Click on the Enable Git's Code Search tab and paste the copied command and submit </h4></u><br/>
        <img src="./static/pastecurl.png" width="900px">`
        }
        if(tabName==='EnGitSearch'){
            modal.style.display = "block";
            textForModal = document.getElementById("abtTab");
            textForModal.innerHTML=`
            <h3>Paste your Curl Command Here</h3>
            <textarea rows="4" cols="90" id="CurlCommand">
</textarea><br/>
<span id="resultFromCurl"></span><br/>
<button onclick="getCurlCommand()">Submit</button>`
            }           



    span.onclick = function () {
        modal.style.display = "none";
    }

    window.onclick = function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    }


}

document.addEventListener("DOMContentLoaded", function(event) {
   
    var langSelection = $("#langSelection").val();

        var iframeCode=document.getElementById('interCompPlace');
        iframeCode.innerHTML=`<iframe height="900px" width="100%" src="https://repl.it/repls/CookedPreviousWorker?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>`;

        

        
    
        document.getElementById('langSelection').addEventListener('change',function(){
            var langSelection = $("#langSelection").val();
            if (langSelection==='PHP'){
                var iframeCode=document.getElementById('interCompPlace');
                iframeCode.innerHTML=`<iframe height="900px" width="100%" src="https://repl.it/repls/CookedPreviousWorker?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>`
            }
            if (langSelection==='Python'){
                var iframeCode=document.getElementById('interCompPlace');
                iframeCode.innerHTML=`<iframe height="900px" width="100%" src="https://repl.it/repls/BriskSingleHashmap?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>`
        
            }

            if (langSelection==='Javascript'){
                var iframeCode=document.getElementById('interCompPlace');
                iframeCode.innerHTML=`<iframe height="900px" width="100%" src="https://repl.it/repls/FixedWearableTests?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>`;
                

            }
            if (langSelection==='NodeJs'){
                var iframeCode=document.getElementById('interCompPlace');
                iframeCode.innerHTML=`<iframe height="900px" width="100%" src="https://repl.it/repls/HarmfulSlateblueSpyware?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>`;




            }
            if (langSelection==='Java'){
                var iframeCode=document.getElementById('interCompPlace');
                iframeCode.innerHTML=`<iframe height="900px" width="100%" src="https://repl.it/repls/MutedPeskyNetworks?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>`;

            }
            
        
        });

    


});

