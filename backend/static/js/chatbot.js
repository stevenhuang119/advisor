function add_row_right(text) {
    const div = document.createElement('div'); 
    
    div.className = 'row'; 

    div.innerHTML = "<p align='right'>" + text + "</p>"; 

    document.getElementById('first_div').appendChild(div);
}

function add_row_left(text) {
    const div = document.createElement('div'); 
    
    div.className = 'row'; 

    div.innerHTML = "<p>" + text + "</p>"; 

    document.getElementById('first_div').appendChild(div);
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