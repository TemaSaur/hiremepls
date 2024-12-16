export default function Button({active=true, onClick=null, children}) {
    const color = active ? 'bg-[#AAAEFF]' : 'bg-[#E5E5EB]'
    return <button onClick={onClick} className={`cursor rounded-lg py-1 px-4 ${color} w-fit`}>
        {children}
    </button>
}