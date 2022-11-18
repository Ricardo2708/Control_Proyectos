function loadJs(file, callback) {
    // Evitar cargar más de 1 vez
    if(document.querySelector(`script[src="${file}"]`)) {
      // Ya se cargó el script, solo se ejecuta la función de retorno
      if(typeof callback == 'function') {
        callback();
      }
    } else {
      // No se ha cargado, primero creas el elemento
      let script = document.createElement('script');
      // Si hay función de retorno
      if(typeof callback == 'function') {
        // Debe ejecutarse cuanto el script se haya cargado
        script.addEventListener('load', callback);
      }
      // Asignar ubicación del script
      script.src = file;
      // Agregar a <head>
      document.head.appendChild(script);
    }
}

let jqCdn = '//cdn.jsdelivr.net/npm/sweetalert2@11';
let jqCdn2 = 'https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js'
let jqCdn3 = "https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" 
let jqCdn4 = 'https://cdn.plyr.io/3.7.2/plyr.js'

$(document).ready(function() {

  $(".btn-block").addClass("message")

  loadJs(jqCdn, () => {
      $(".message").click(function (e) {
          let timerInterval
          Swal.fire({
          title: 'Validando.....',
          html: 'Tiempo Restante: <b></b>',
          timer: 2000,
          timerProgressBar: true,
          didOpen: () => {
              Swal.showLoading()
              const b = Swal.getHtmlContainer().querySelector('b')
              timerInterval = setInterval(() => {
              b.textContent = Swal.getTimerLeft()
              }, 100)
          },
          willClose: () => {
              clearInterval(timerInterval)
          }
          }).then((result) => {
          /* Read more about handling dismissals below */
          if (result.dismiss === Swal.DismissReason.timer) {
              console.log('I was closed by the timer')
          }
          })
      });
      $(".soporte").click(function (e){
        e.preventDefault()
        Swal.fire({
          title: 'Deseas Comunicarte Con Nosotros?',
          text: "Te Ayudaremos A Que Resuelvas Tus Problemas",
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Comunicar'
        }).then((result) => {
          if (result.isConfirmed) {
            window.open('https://api.whatsapp.com/send?phone=60447112', '_blank')

            
          }
        })
      })

      $.ajax({
        method: 'GET',
        url: '/inicio2/',
        dataType: "json",
        success: function(response) {
          const mensaje = response.Mensajes;

          if(localStorage.getItem("numero_notificacion") == mensaje.length){
            var myEl = document.getElementById('notificacion');
            if(localStorage.getItem("notificacion")){
              $("#div-red").removeClass("icono-rojo")
            }
            myEl.addEventListener('click', function() {
              localStorage.setItem("notificacion", true);
              $("#div-red").removeClass("icono-rojo")
            });
          }
          else{
            localStorage.setItem("numero_notificacion", mensaje.length);
            $("#div-red").addClass("icono-rojo")
            localStorage.removeItem("notificacion");

            var myEl = document.getElementById('notificacion');
            myEl.addEventListener('click', function() {
              localStorage.setItem("notificacion", true);
              $("#div-red").removeClass("icono-rojo")
            });
            

            const Toast = Swal.mixin({
              toast: true,
              position: 'top-end',
              showConfirmButton: false,
              timer: 3000,
              timerProgressBar: true,
              didOpen: (toast) => {
                toast.addEventListener('mouseenter', Swal.stopTimer)
                toast.addEventListener('mouseleave', Swal.resumeTimer)
              }
            })
          
            Toast.fire({
              icon: 'info',
              title: 'Tienes Nuevas Notificaciones'
            })
            
          }





          
        },
        error: function(response){
          console.log(response);
        }
      });
  });

  loadJs(jqCdn4, () =>{
    $(".content-header").addClass("contenido")
    
    function direccionPrincipal(){
      
      var direccion2 = window.location;
      if(direccion2.pathname == '/'){
        $.ajax({
          method: 'GET',
          url: '/inicio/',
          dataType: "json",

          success: function(response){
            const proyecto = response.proyecto
            const div3 = document.querySelector(".contenido").insertAdjacentHTML("afterend",
            `
            <div class="help-video">
              <div class="contenido-video">
                <h2>¿Como Usar La Plataforma?</h2>
                <p>
                  En esta seccion te enseñaremos a usar la plataforma de manera rapida y sencilla
                  y a la vez utilizando todas sus herramientas 
                </p>

                <p>
                  Si tienes problemas con el sitio o has detectado algun error comunicate inmediatamente
                  con nosotros para poder ayudarte
                </p>
    
                <div class="enlaces-inicio">
                  
                  <a href="#" class="btn btn-primary btn-ayuda soporte">Contactanos Ahora</a>
                </div>
              </div>
              <video id="player" class="video" playsinline controls>
                <source src="static/video/video1.mp4" type="video/mp4" />
              </video>
            </div>
            <br>
    
            <h3 class="titulo-estadisticas">${proyecto}</h3>
            <p class="texto-estadisticas">Las estadisticas se muestran en tiempo real</p>
            <div class="graficos">
          
              
              <div class="contenedor-grafica grafica-reducir">
                <canvas id="grafica2" width="200" heigth="100"></canvas>
              </div>

              <div class="contenedor-grafica">
                <canvas id="grafica" width="200" heigth="100"></canvas>
              </div>
    
              <div class="contenedor-grafica grafica-reducir">
                <canvas id="grafica3" width="200" heigth="100"></canvas>
              </div>
    
            </div>
            <br/>
    
        
            `);
          },

          error: function(response){
            console.log(response);
          }

        })
        
      }
      $.ajax({
        method: 'GET',
        url: '/inicio/',
        dataType: "json",

        success: function(response){
          if(direccion2.pathname == response.path){
            const proyecto = response.proyecto
            const div3 = document.querySelector(".contenido").insertAdjacentHTML("afterend",
            `
            <div class="graficos">
              <div class="contenedor-grafica grafica-reducir">
                <canvas id="grafica2" width="200" heigth="100"></canvas>
              </div>

              <div class="contenedor-grafica">
                <canvas id="grafica" width="200" heigth="100"></canvas>
              </div>

              <div class="contenedor-grafica grafica-reducir">
                <canvas id="grafica3" width="200" heigth="100"></canvas>
              </div>
            </div>
            <br/>
    
        
            `);
          }

        },

        error: function(response){
          console.log(response);
        }

      })

      
    }
    direccionPrincipal()
    
  })

  $(document).ready(function(){
    loadJs(jqCdn2, () =>{
      $.ajax({
        method: 'GET',
        url: '/inicio/',
        dataType: "json",
        success: function(response) {
          const inicio = response.inicio.length
          const cobro = response.cobro.length
          const final = response.final.length
          

          // Estado Contratistas
          const activo = response.activo.length
          const inactivo = response.inactivo.length

          // Porcentajes

          const porcentaje1 = response.porcentaje1.length
          const porcentaje2 = response.porcentaje2.length
          const porcentaje3 = response.porcentaje3.length

          
            let grafico = document.getElementById('grafica').getContext('2d')
            var chart1  = new Chart(grafico,{
              type:"bar",
              data:{
                labels:['Inicio', 'Cobro', 'Final'],
                datasets:[
                  {
                    label: `Estado De Obras`,
                    backgroundColor: [
                      'rgba(255, 99, 132, 0.7)',
                      'rgba(255, 159, 64, 0.7)',
                      'rgba(75, 192, 192, 0.7)',
                      'rgba(54, 162, 235, 0.2)',
                      'rgba(153, 102, 255, 0.2)',
                      'rgba(201, 203, 207, 0.2)'
                    ],
                    borderColor: [
                      'rgb(255, 99, 132)',
                      'rgb(255, 159, 64)',
                      'rgb(75, 192, 192)',
                      'rgb(54, 162, 235)',
                      'rgb(153, 102, 255)',
                      'rgb(201, 203, 207)'
                    ],
                    borderWidth: 1,
                    data:[inicio,cobro,final],
                  }
                ]
              },
              options: {
                indexAxis: 'x',
              }
            })
        
            let grafico2 = document.getElementById('grafica2').getContext('2d')
            var chart2 = new Chart(grafico2,{
              type:"polarArea",
              data:{
                labels:['Cambio De Contratista | Activo', 'Cambio De Contratista | Inactivo'],
                datasets:[
                  {
                    label:`Numero De Registros`,
                    backgroundColor: [
                      'rgb(255, 99, 132)',
                      'rgb(54, 162, 235)',
                      'rgb(255, 205, 86)',
                      'rgba(153, 102, 255)',
                      'rgb(255, 205, 86)'
                    ],
                    borderColor: [
                      'rgb(255, 99, 132)',
                      'rgb(54, 162, 235)',
                      'rgb(255, 205, 86)',
                    ],
                    borderWidth: 1,
                    data: [activo, inactivo],
                  }
                ]
              }

            })

            let grafico3 = document.getElementById('grafica3').getContext('2d')
            var chart3 = new Chart(grafico3,{
              type:"doughnut",
              data:{
                labels:['Pago:100%', 'Pago:50%', 'Pago:0%'],
                datasets:[
                  {
                    label: "Contratistas",
                    backgroundColor: [
                      'rgb(255, 99, 132)',
                      'rgb(54, 162, 235)',
                      'rgb(255, 205, 86)'
                    ],
                    borderWidth: 1,
                    data:[porcentaje3,porcentaje2,porcentaje1],
                  }
                ]
              }

            })
          

          
        },
        error: function(response){
          console.log(response);
        }
      }); 
    })
  });

  function notificacion(){
    $.ajax({
      method: 'GET',
      url: '/inicio2/',
      dataType: "json",
      success: function(response) {
        const mensaje = response.Mensajes;
        if(mensaje.length > 0){
          $(".alerta").addClass("notificacion-on")
          const div5 = document.querySelector(".ml-auto li").insertAdjacentHTML("afterend",
          `
            <div id="div-red" class="alerta-noti icono-rojo"></div>
            <i type="button" id=notificacion class="fa-solid fa-bell notificacion alerta"  data-toggle="modal" data-target="#exampleModal" ></i>
          `);
        }
        else{
          const div5 = document.querySelector(".ml-auto li").insertAdjacentHTML("afterend",
          `
            <i type="button" class="fa-regular fa-bell notificacion "  data-toggle="modal" data-target="#exampleModal"></i>
          `);
        }
        mensaje.forEach(element => {
          const nombre = element[0];
          const contenido = element[1];
          const fecha = element[2];

          const fechaActual = new Date();
          const formato = fechaActual.toLocaleDateString('en-us', fecha);
          
          const div6 = document.querySelector(".wrapper").insertAdjacentHTML("beforeend",
          `
          <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header modal-mensaje">
                  <h5 class="modal-title" id="exampleModalLabel">Notificaciones</h5>
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                  </button>
                </div>
      
                <div class="mensaje-card">

                </div>
              
              </div>
            </div>
          </div>
          `);

          let div = document.createElement('div')
            div.className = "modal-body contenedor-mensaje";
            div.innerHTML = `
            <img class="img-usuario-notificacion" src="https://cdn-icons-png.flaticon.com/512/5776/5776085.png"/>
            <div class="contenido-mensaje">
              <h2>${nombre}</h2>
              <p>${contenido}</p>
              <p class="fecha">Fecha De Publicacion: <span>${formato}</span></p>
            </div>
            `
          document.querySelector('.mensaje-card').appendChild(div)


        });
      },
      error: function(response){
        console.log(response);
      }
    });



  }
  notificacion()

  try{
    
    const div = document.querySelector(".login-box-msg").innerHTML = `
    <h4 class="login-texto">Sistema / Control De Proyectos</h4>
    <p class="texto-contraseña">Porfavor Ingrese Su Usuario:</p>`; 
  
    const div2 = document.querySelector(".card-body").insertAdjacentHTML("afterend",
    `<a class="cambio-contraseña" href="#">¿Has Olvidado Tu Contraseña?</a>`);
  
  }
  catch{
  
  }
  
  const div4 = document.querySelector("link").insertAdjacentHTML("afterend",
  `<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css">
   <link rel="stylesheet" href="https://cdn.plyr.io/3.7.2/plyr.css" />
  `);

  // const div6 = document.querySelector(".user-panel .image").innerHTML=
  // `
  //   <img src="https://cdn-icons-png.flaticon.com/512/3177/3177440.png" width="160px" class="img-circle elevation-2" alt="User Image">
  // `;
});


