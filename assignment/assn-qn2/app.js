
//required modules
const bodyParser = require("body-parser");
const express = require("express");
var fs = require("fs");
const app = express();
app.use(express.static("public"));
app.use(
  bodyParser.urlencoded({
    extended: true,
  })
);
app.use(bodyParser.json());

//sends maain.html whenever a get request is made (i.e., searching for localhost:3000 on web)
app.get("/", function (req, res) {
  res.sendFile(__dirname + "/maain.html");
});

//collects the data sent using POST method to url "/send"
app.post("/send",function(req,res){


  // Reading JSON file
  const users = require("./input");

  // Defining new user
  let user = {
    "username": req.body.user,
    "latitude":req.body.lat,
    "longitude":req.body.lng
  };
  console.log(req.body)

  // Adding new data to users object 
  users.push(user);

  // STEP 3: Writing to a json file(input.json)
  fs.writeFile("input.json", JSON.stringify(users), (err) => {
    // Checking for errors
    if (err) throw err; 

    console.log("Done writing");
    res.redirect("/") // Success
});

})

app.listen(3000, function () {
  console.log("server started");
});
