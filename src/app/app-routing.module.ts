import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FillformComponent } from './fillform/fillform.component';
import { LoginComponent } from './login/login.component';

const routes: Routes = [
  {path:'fillform',component:FillformComponent,},
  {path:'login',component:LoginComponent},
  {path:'',component:LoginComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
