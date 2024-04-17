import { AfterContentInit, Component, ContentChild, Host, OnInit } from '@angular/core';
import { EmployeeComponent } from '../employee/employee.component';
import { RoomsService } from '../rooms/services/rooms.service';

@Component({
  selector: 'hinv-container',
  templateUrl: './container.component.html',
  styleUrls: ['./container.component.css'],
  // providers: [RoomsService]
})
export class ContainerComponent implements OnInit, AfterContentInit {

  @ContentChild(EmployeeComponent) employee !: EmployeeComponent

  // @Host() -> in case we want seperate instance of roomsService
  // for each container
  // constructor(@Host() private roomsService: RoomsService) {}
  constructor() {}


  ngOnInit(): void {
    
  }

  ngAfterContentInit(): void {
    console.log(this.employee);
    this.employee.empName = 'Renato'
  }
}
