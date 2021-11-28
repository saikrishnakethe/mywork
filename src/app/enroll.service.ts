import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { user } from './fillform/user';
import { catchError } from 'rxjs';
import { throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EnrollService {
  _url='http://localhost:3000/enroll';

  constructor(private _http:HttpClient) { 
  }
  enroll(user:user){
    return this._http.post<any>(this._url,user)
    .pipe(catchError(this.errorhandler))

  }
  errorhandler(error:HttpErrorResponse){
    return throwError(error);
  }
}
