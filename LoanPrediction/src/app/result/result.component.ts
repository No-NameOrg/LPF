import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css']
})
export class ResultComponent implements OnInit {

  constructor() { }
  model1 = '';
  ngOnInit(): void {
    this.model1 = localStorage.getItem('model1');
    
  }

}
