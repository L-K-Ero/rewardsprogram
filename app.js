
//var MEMBERS = {}
var loadallthedata = function () {
    fetch("https://iceboxrewards.herokuapp.com/").then(function (response) {
	console.log("server responded.");
	response.json().then(function (data) {
	    console.log("data recieved from server:", data);
	    var databaselist = document.querySelector("#members");
	    databaselist.innerHTML = "";
	    data.forEach( function (member) {
                    // li contains a object
		var newListItem = document.createElement("li");
                    // h3 is title of object
                var titleHeading = document.createElement("h3");
                    // puts restaruant name as title: 
                titleHeading.innerHTML = member.NAME;
                newListItem.appendChild(titleHeading);

                titleHeading.onclick = function () {
                    titleHeading.setAttribute("contenteditable", true);
                }

                var theemail = document.createElement("p");
                theemail.innerHTML = member.EMAIL;
                newListItem.appendChild(theemail);

                theemail.onclick = function () {
                    theemail.setAttribute("contenteditable", true);                }

                var thephone = document.createElement("p");
                thephone.innerHTML = member.PHONE;
                newListItem.appendChild(thephone);

                thephone.onclick = function () {
                    thephone.setAttribute("contenteditable", true);
                }

                var thebirthday = document.createElement("p");
                thebirthday.innerHTML = member.BIRTHDAY;
                newListItem.appendChild(thebirthday);

                thebirthday.onclick = function () {
                    thephone.setAttribute("contenteditable", true);
                }
                
                var thezip = document.createElement("p");
                thezip.innerHTML = member.ZIPCODE;
                newListItem.appendChild(thezip);

                thezip.onclick = function () {
                    thezip.setAttribute("contenteditable", true);
                }

                var statuslevel = document.createElement("p");
                statuslevel.innerHTML = member.LEVEL;
                newListItem.appendChild(statuslevel);

                statuslevel.onclick = function () {
                    statuslevel.setAttribute("contenteditable", true);
                }
                    // puts all that in parent objects. 
                
                var deleteButton = document.createElement("BUTTON");
                deleteButton.innerHTML = "Delete";
                deleteButton.onclick = function () {
                    var result = confirm("Want to delete?");
                    if (result) {
                        deleteMembers(member.rowid); 
                    };
                    //check syntax
                };
                newListItem.appendChild(deleteButton);

                var editButton = document.createElement("BUTTON");
                editButton.innerHTML = "Edit";
                editButton.onclick = function () {
                    editThing(titleHeading.innerHTML, theemail.innerHTML, thephone.innerHTML, thebirthday.innerHTML, thezip.innerHTML, statuslevel.innerHTML, member);
                };
                newListItem.appendChild(editButton);
		databaselist.appendChild(newListItem);
	});

	});
});
};

loadallthedata();


var SendinfoButton = document.querySelector("#register_new_member");
SendinfoButton.onclick = function () {
   
    var new_name = document.querySelector("#new_member_name").value;
    var new_email = document.querySelector("#new_member_email").value;
    var new_phone = document.querySelector("#new_member_phone").value;
    var new_birthday = document.querySelector("#new_member_birthday").value;
    var new_zipcode = document.querySelector("#new_member_zipcode").value;
    var new_level = document.querySelector("#new_member_level").value;
        // var otherinput = .... 
    // ...
	var bodystr = "name=" + encodeURIComponent(new_name);
        bodystr += "&email=" + encodeURIComponent(new_email);
        bodystr += "&phone=" + encodeURIComponent(new_phone);
        bodystr += "&birthday=" + encodeURIComponent(new_birthday);
        bodystr += "&zipcode=" + encodeURIComponent(new_zipcode);
        bodystr += "&level=" + encodeURIComponent(new_level);

        // bodystr += "thing="+encodeURIComponent( otherinput );
    // ...
    	fetch("https://iceboxrewards.herokuapp.com/", {
        method: "POST",
        body: bodystr,
        headers: {"Content-Type":"application/x-www-form-urlencoded"}
    }).then(function (response) {
        loadallthedata();
    });
	//document.getElementByID("ingredient_input").value = '';
};
// DELETE GOES HERE

var deleteMembers = function( itemID ) {
    fetch( "https://iceboxrewards.herokuapp.com/" + itemID, {
        method: "DELETE"
    }).then(function( response ) {
        loadallthedata(); // based on the fact that i will make the refresh a function. 
    });
};

var editThing = function(editedName, email, phone, birthday, zipcode, level, item ) {
    var bodystr = "name=" + encodeURIComponent(editedName);
    bodystr += "&email=" + encodeURIComponent(email);
    bodystr += "&phone=" + encodeURIComponent(phone);
    bodystr += "&birthday=" + encodeURIComponent(birthday);
    bodystr += "&zipcode=" + encodeURIComponent(zipcode);
    bodystr += "&level=" + encodeURIComponent(level);

    fetch("https://iceboxrewards.herokuapp.com/" + item.rowid, {
        DATABASE_URL = os.nviron['DATABASE_URL']
        method: "PUT", 
        body: bodystr, 
        headers: {"Content-Type":"application/x-www-form-urlencoded"}
    }).then(function( response) {
        loadallthedata();
    });
};
    
// update: 
// starts like get or delete, but sends modified data to the exact url and the server replaces it like a post. 
//
//    database code: UPDATE table SET n=?, b=? WHERE id = ?;


// document.getElementById("ingredient_input").value = '';
//
// CORS cross origin resource sharing
// on server: self.send_header("Access-Control-Allow-Origin","*")
// put this on get post and send post with the other header stuff...
//
// google cors mozilla developer network. stop when you see preflighted requests. 
//
