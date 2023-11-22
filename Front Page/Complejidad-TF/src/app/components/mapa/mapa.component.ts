import { Component } from '@angular/core';
import { ShortestPathService } from 'src/app/shortest-path.service';
import { ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-mapa',
  templateUrl: './mapa.component.html',
  styleUrls: ['./mapa.component.css']
})
export class MapaComponent {

  startStreet: any = {};
  endStreet: any = {};
  shortestPath: any[] = [];  // Asegúrate de que shortestPath sea un array

  constructor(private streetService: ShortestPathService, private cdr: ChangeDetectorRef) { }

  findShortestPath() {
    this.streetService.findShortestPath(this.startStreet, this.endStreet)
      .subscribe(response => {
        if (Array.isArray(response.shortest_path)) {
          this.shortestPath = response.shortest_path;
          this.cdr.detectChanges();  // Forzar la detección de cambios
          console.log('Shortest Path:', this.shortestPath);
        } else {
          console.error('La respuesta no contiene un array shortest_path:', response);
        }
      }, error => {
        console.error('Error al obtener la ruta más corta', error);
        if (error && error.error) {
          console.error('Detalles del error:', error.error);
        }
      });
  }
  
  
}
