import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

const httpOptions = {
  headers: new HttpHeaders({
    'Access-Control-Allow-Origin': 'http://localhost:4200/',
    'Access-Control-Allow-Methods': 'POST',
    'Access-Control-Allow-Headers': 'X-Requested-With,content-type'
  })
};

@Injectable({
    providedIn: 'root'
          })
// const cors = require('cors');
export class LoanService {

  formData = {
    married: '',
    dependents: '',
    applicantIncome: 0,
    coApplicantIncome: 0,
    loanAmount: 0,
    loanAmountTerm: 0,
    creditHistory: 0,
    propertyArea: '',
  };
  constructor(private hc: HttpClient) { }

  sendData(data): Observable<Object>
  {
        this.formData = data;
        // tslint:disable-next-line:radix
        this.formData.creditHistory = parseInt(data.creditHistory);
        console.log(this.formData);
        const headers = new Headers();
        headers.append('Access-Control-Allow-Origin', '*');
        headers.append('Access-Control-Allow-Methods', 'POST');
        headers.append('Access-Control-Allow-Headers', 'X-Requested-With,content-type');

        return this.hc.post('http://127.0.0.1:5000/', this.formData, httpOptions);

  }
}
