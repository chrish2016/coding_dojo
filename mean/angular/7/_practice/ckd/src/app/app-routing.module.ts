import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LandingComponent } from './landing/landing.component';
import { HomeComponent } from './home/home.component';
import { UserComponent } from './user/user.component';
import { UserPublicComponent } from './user/user-public/user-public.component';
import { UserPrivateComponent } from './user/user-private/user-private.component';

const routes: Routes = [
  { path: '',  pathMatch: 'full', component: LandingComponent },
  { path: 'home', component: HomeComponent },
  { path: 'user', component: UserComponent, children:[
    { path: 'public', component: UserPublicComponent },
    { path: 'private', component: UserPrivateComponent },
  ]},
  { path: 'gohome', redirectTo: '/home' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
