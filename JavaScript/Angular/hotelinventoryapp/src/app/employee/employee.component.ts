import { Component, OnInit, Self } from '@angular/core';
import { RoomsService } from '../rooms/services/rooms.service';

@Component({
  selector: 'hinv-employee',
  templateUrl: './employee.component.html',
  styleUrls: ['./employee.component.css'],
  // set as providers for this component to
  // have its own instance of servie
  // or if want only one single instance-> no need 
  // line below
  providers: [RoomsService]
})
export class EmployeeComponent implements OnInit {

  empName: string = "Iris"

  // @Self() - if there is this decorator then Angular will 
  // not go up to app.ts to look for RoomsService
  // only check if RoomsService is available only in this file
  constructor (@Self() private roomsService: RoomsService) {}
  
  ngOnInit(): void {
    
  }
}
