<script lang="ts">
    function openConfirm(){
        (document.getElementById('confirm_modal') as HTMLDialogElement)?.showModal();
    }
    async function clearGopros() {
        try {
            await fetch('http://localhost:8000/controls/clear_gopros');
        } catch (err) {
            console.error('Failed to fetch status:', err);
        }
    }
    async function setKeepAlive() {
        try {
            await fetch('http://localhost:8000/controls/set_keep_alive');
        } catch (err) {
            console.error('Failed to fetch status:', err);
        }
    }

</script>

<div class="p-4 rounded-box shadow-sm bg-base-200">
    <h1 class="text-2xl m-2 font-bold text-content">Extra Controls</h1>
    <div class="grid gap-2 grid-cols-2 sm:grid-cols-3">
        <button class="btn btn-block" onclick={openConfirm}>
            Clear GoPro
        </button>
        <button class="btn btn-block" onclick={setKeepAlive}>
            Keep Alive
        </button>
    </div>
</div>
<dialog id="confirm_modal" class="modal">
    <div class="modal-box">
        <h1 class="text-xl sm:text-2xl font-bold">Clear Gopros?</h1>
        <p class="text-md sm:text-lg">Would you like to clear to GoPros?</p>
        <div class="modal-action">
            <form onsubmit={
                ()=>{
                    clearGopros();
                    (document.getElementById('confirm_modal') as HTMLDialogElement)?.close();
                }
            }>
                <button class="btn btn-block btn-error w-full">Clear</button>
            </form>
            <form method="dialog">
                <button class="btn">Close</button>
            </form>
        </div>
    </div>
</dialog>
