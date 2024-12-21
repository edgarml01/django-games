document.addEventListener("DOMContentLoaded", function () {
    // Inicializar el modal de bienvenida
    const bienvenidaModalElement = document.getElementById("bienvenidaModal");

    if (bienvenidaModalElement) {
        const bienvenidaModal = new bootstrap.Modal(bienvenidaModalElement);

        // Mostrar automáticamente el modal al cargar la página
        bienvenidaModal.show();

        // Opcional: Evento para registrar cuando se cierra el modal
        bienvenidaModalElement.addEventListener("hidden.bs.modal", function () {
            console.log("El modal de bienvenida ha sido cerrado.");
        });
    } else {
        console.error("No se encontró el modal de bienvenida.");
    }
});
