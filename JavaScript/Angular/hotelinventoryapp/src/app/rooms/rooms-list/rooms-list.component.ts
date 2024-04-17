import { ChangeDetectionStrategy, Component, EventEmitter, Input, OnChanges, OnDestroy, OnInit, Output, SimpleChanges } from '@angular/core';
import { RoomList } from '../rooms';

@Component({
  selector: 'hinv-rooms-list',
  templateUrl: './rooms-list.component.html',
  styleUrls: ['./rooms-list.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class RoomsListComponent implements OnInit, OnChanges, OnDestroy {
  
  
  @Input() rooms: RoomList[] | null = []

  @Input() title: string = ''

  @Output() selectedRoom = new EventEmitter<RoomList>()

  constructor(){

  }

  ngOnInit(): void {
    
  }

  ngOnChanges(changes: SimpleChanges): void {
    console.log(changes);
    if(changes['title']){
      this.title = changes['title'].currentValue.toUpperCase()
    }
  }

  ngOnDestroy(): void {
    console.log('destroy');
    
  }

  selectRoom(room: RoomList){
    this.selectedRoom.emit(room)
    // this.selectedRoom = room
  }
}
