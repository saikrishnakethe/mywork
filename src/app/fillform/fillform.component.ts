import { Component, OnInit } from '@angular/core';
import { user } from './user';
import { EnrollService } from '../enroll.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-fillform',
  templateUrl: './fillform.component.html',
  styleUrls: ['./fillform.component.css']
})
export class FillformComponent implements OnInit {
  submitted=false;

  userdata=new user("sai krishna","3-63,leelanagar","nuzvid","Andhrapradesh",521201,"India")
  errormsg='';

  constructor(private _enrollmentservice:EnrollService,private router:Router) { }

  ngOnInit(): void {
  }
  onsubmit(){

    this._enrollmentservice.enroll(this.userdata)
    .subscribe(data=>console.log("sucess!",data),
    error=>this.errormsg=error.statusText)
  }

  filled(){
    this.router.navigate(["display"]);
  }

}
