import { Component } from '@angular/core';
import { ShortestPathService } from 'src/app/shortest-path.service';


@Component({
  selector: 'app-mapa',
  templateUrl: './mapa.component.html',
  styleUrls: ['./mapa.component.css']
})
export class MapaComponent {

  startStreet: any = {};
  endStreet: any = {};
  shortestPath: any = {};

  constructor(private streetService: ShortestPathService) { }

  findShortestPath() {
    this.streetService.findShortestPath(this.startStreet, this.endStreet)
      .subscribe(response => {
        this.shortestPath = response.shortest_path;
      });
    }
}
