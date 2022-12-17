import logo from './logo.svg';
// import './App.css';
import "./main.js"
import añadirRegla from "./controllers/añadirRegla"


function App() {
  return (
    <div className="App">
      <header className="App-header">
      <div id="content">
        <p>Directorio: "C:/Usuario/Documentos/CarpetaDesordenada"</p>
        <button className="btn btn-primary">...</button>
        <form>
            <div class="form-group">
                <div class="mb-3">
                    <label for="Extensiones de Archivo" class="form-label">Extensiones de archivo</label>
                    <input type="text" class="form-control" name="" id="inputExtensiones"
                        placeholder=".mp4, .mkv, .flv"></input>
                </div>

                <div class="mb-3">
                    <label for="" class="form-label">Tipo de archivo</label>
                    <input type="text" class="form-control" name="" id="inputTipo" placeholder="Videos"></input>
                </div>

                <div class="mb-3">
                    <label for="" class="form-label">Direccion de destino</label>
                    <input type="text" class="form-control" name="" id="inputDireccion"
                        placeholder="C:/Usuario/Videos"></input>
                </div>

            </div>

            <button class="btn btn-primary" id="addButton" onClick={añadirRegla}>Añadir Regla</button>
        </form>
        <table className="table">
            <thead>
                <tr>
                    <th scope="col"><input className="form-check-input" type="checkbox"></input></th>
                    <th scope="col">Extensiones de archivo</th>
                    <th scope="col">Nombre del tipo</th>
                    <th scope="col">Direccion de destino</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th scope="col"><input className="form-check-input" type="checkbox"></input></th>
                    <th scope="row">.jpg</th>
                    <td>Imagenes</td>
                    <td>C:/Usuario/Imagenes</td>
                </tr>
                <tr>
                    <th scope="col"><input className="form-check-input" type="checkbox"></input></th>
                    <th scope="row">.mp4</th>
                    <td>Videos</td>
                    <td>C:/Usuario/Videos</td>
                </tr>
                <tr>
                    <th scope="col"><input class="form-check-input" type="checkbox"></input></th>
                    <th scope="row">.mp3</th>
                    <td>Musica</td>
                    <td>C:/Usuario/Musica</td>
                </tr>
            </tbody>
        </table>
        <button class="btn btn-primary"> Mover archivos </button>
        <br></br>

        <div id="logger" class="log">
        </div>

        <a href="/">
            <i class=" fa-3x fa-solid fa-gear"></i>
        </a>
    </div>
      </header>
    <script src="main.js"></script>
    </div>
  );
}

export default App;
