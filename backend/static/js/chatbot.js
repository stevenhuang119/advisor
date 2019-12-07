function add_row_right(text) {
    const div = document.createElement('div'); 
    
    div.className = 'row right-chat'; 

    div.innerHTML = "<div class='panel panel-default'><div class='panel-body right-panel-body' align='right'>" + text + "</div></div>"; 

    var obj = document.getElementById('chat_body');

    obj.appendChild(div); 
    obj.scrollTop = obj.scrollHeight;
}

function add_row_left(text) {
    const div = document.createElement('div'); 
    
    div.className = 'row left-chat'; 

    div.innerHTML = "<div class='panel panel-default'><div class='panel-body left-panel-body'>" + text + "</div></div>"; 

    var obj = document.getElementById('chat_body');

    obj.appendChild(div);
    obj.scrollTop = obj.scrollHeight; 
}

function change_frame(dept, course) {
    if (dept != "null" && course != "null"){
        url = "https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=w_20_2270&cgtype=ug&show=20&department=" + dept + "&catalog=" + course;
        console.log(url); 

        linkText = "Click here for more details on " + dept + " " + course; 

        // document.getElementById('course_frame').src = url;
        document.getElementById('site_link').href = url;
        document.getElementById('site_link').text = linkText; 
    }

     
}


function input_text() {
    var text = document.getElementById('chat_text').value;
    console.log(typeof text);
    add_row_right(text); 

    $.getJSON('/_clinc_process', {text: text}, function(data) {
        console.log(data.result)
        console.log(data.dept);
        console.log(data.course); 

        add_row_left(data.result); 
        change_frame(data.dept, data.course)
    }
    );

}