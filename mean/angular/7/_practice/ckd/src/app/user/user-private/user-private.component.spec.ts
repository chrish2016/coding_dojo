import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UserPrivateComponent } from './user-private.component';

describe('UserPrivateComponent', () => {
  let component: UserPrivateComponent;
  let fixture: ComponentFixture<UserPrivateComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UserPrivateComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UserPrivateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
