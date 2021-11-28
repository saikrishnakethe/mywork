import { Component, OnInit } from '@angular/core';

import {Router} from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  username:string;
  password:string;
  routerLinkVariable:string;

  constructor(private router: Router) { 
  }

  ngOnInit() {
  }



  login() : void {
    if(this.username == 'saikrishnakethe@gmail.com' && this.password == 'sai@1818'){
     this.router.navigate(["fillform"]);
     //this.routerLinkVariable="/fillform";
    }else {
      alert("Invalid credentials");
    }
  }
  }