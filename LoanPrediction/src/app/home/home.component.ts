import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import {LoanService} from '../loan.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  data = {
    married: '',
    dependents: '',
    applicantIncome: '',
    coApplicantIncome: '',
    loanAmount: '',
    loanAmountTerm: '',
    creditHistory: '',
    propertyArea: '',
  };
 
  constructor(private router: Router, private ds: LoanService) { }

  ngOnInit(): void {

  }

onSubmit(): void
{

 this.ds.sendData(this.data).subscribe((res) => {
   console.log(res);
   res['logPred'] 
   localStorage.setItem('LogisticRegression', res['logPred']);
   localStorage.setItem('DecisionTree', res['DecPred']);
   this.router.navigateByUrl('/result');
  });


}
}
