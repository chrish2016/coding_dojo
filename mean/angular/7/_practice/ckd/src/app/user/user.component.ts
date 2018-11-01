import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {

  constructor( private _route: ActivatedRoute ) {
    this._route.paramMap.subscribe( (params) => {
      console.log(params.get('id'));
    })
  }

  ngOnInit() {
  }

}
