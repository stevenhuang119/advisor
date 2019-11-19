function add_row_right(text) {
    const div = document.createElement('div'); 
    
    div.className = 'row'; 

    div.innerHTML = "<div class='panel panel-default'><div class='panel-body' align='right'>" + text + "</div></div>"; 

    document.getElementById('chat_body').appendChild(div);
}

function add_row_left(text) {
    const div = document.createElement('div'); 
    
    div.className = 'row'; 

    div.innerHTML = "<div class='panel panel-default'><div class='panel-body'>" + text + "</div></div>"; 

    document.getElementById('chat_body').appendChild(div);
}


function input_text() {
    var text = document.getElementById('chat_text').value;
    console.log(typeof text);
    add_row_right(text); 

    $.getJSON('/_clinc_process', {text: text}, function(data) {
        console.log(data.result); 
        add_row_left(data.result); 
    }
    );

}