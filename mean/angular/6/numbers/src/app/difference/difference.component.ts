import { Component, OnInit } from '@angular/core';
import { TotalService } from '../total.service';

@Component({
  selector: 'app-difference',
  templateUrl: './difference.component.html',
  styleUrls: ['./difference.component.css']
})
export class DifferenceComponent implements OnInit {
  numbers: number[] = [];
  totalnumbers: number[] = [];
  

  constructor(private _totalService: TotalService) { }

  ngOnInit() {
    this.totalnumbers = this._totalService.retrieveTotalNumbers();
  }
  pushTotal(num: number) {
    this._totalService.TotalNumber();
  }
}
