const express=require('express')
const bodyparser=require('body-parser')
const cors=require('cors')
const mysql=require('mysql');


var connection = mysql.createConnection({
    host: "localhost",
    user: "root",
    database: "address"
  });


  let output;
  
  const setOutput = (rows) => {
      output = rows;
      console.log(output);
  }


let x=100;
let y="sai";


const port=3000;
const app=express();
app.use(bodyparser.json());
app.use(cors());

app.get('/',(req,res,next)=>{
    const q="select * from addressbook";
	connection.query(q,(err,result,fields)=>{
        if(err) throw err;
        //var count=result[0].count;
        //res.send("we have "+count+" users");
        res.send("ss!!");
	})
});


const q="select * from addressbook";
connection.query(q,(err,result,fields)=>{
    if(err) throw err;
    //var count=result[0].count;
    //res.send("we have "+count+" users");
    setOutput(result);
});

app.post('/enroll',(req,res)=>{
    console.log(req.body);
    const q=[]
    q.push([req.body.fullname,req.body.address,req.body.city,req.body.state,req.body.postalcode,req.body.country]);

    connection.query("insert into addressbook (fullname,address,city,state,postalcode,country) values ?",[q],(err,result,fields)=>{
		if(err) throw err;
		console.log(result);
	})
    res.status(401).send({"message":"datareceived"});
})



app.listen(port,()=>{
    console.log("server running on"+port);
});

console.log("x:"+x+"y:"+y);



