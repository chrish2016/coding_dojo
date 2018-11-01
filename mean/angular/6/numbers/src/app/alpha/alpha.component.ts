import { Component, OnInit } from '@angular/core';
import { TotalService } from '../total.service';

@Component({
  selector: 'app-alpha',
  templateUrl: './alpha.component.html',
  styleUrls: ['./alpha.component.css']
})
export class AlphaComponent implements OnInit {
  numbers: number[] = [];
  alphanumbers: number[] = [];

  constructor(private _totalService: TotalService) { }

  ngOnInit() {
    this.alphanumbers = this._totalService.retrieveAlphaNumbers();
  }
  
  pushAlpha(num: number) {
    this._totalService.addAlphaNumber();
  }
}
