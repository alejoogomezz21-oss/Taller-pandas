from pathlib import Path

PROCESSED = Path(__file__).parent / "Data" / "processed"


def validar_premerge(clientes, ventas):
    ok = True
    """Revisa que el merge se pueda hacer. Devuelve True si todo está bien, False si no.

    Revisar:
    - Que exista la columna "id_cliente" en los dos dataframes.
    - Que "id_cliente" no esté repetido en clientes.
    - Que "id_cliente" tenga el mismo tipo en los dos dataframes.
    - Cuántas ventas no tienen cliente asociado (esto solo se informa, no falla).
    """

    # TODO 6: escribir las validaciones y devolver True o False.
    # 1.
    if "id_cliente" not in clientes.columns or "id_cliente" not in ventas.columns:
        print("[validación] ERROR: falta la columna id_cliente.")
        return False

    # 2.
    repetidos = clientes["id_cliente"].duplicated().sum()
    if repetidos > 0:
        print(f"[validación] ERROR: hay {repetidos} id_cliente repetidos en clientes.")
        ok = False
    else:
        print("[validación] OK: id_cliente es único en clientes.")

    # 3.
    if clientes["id_cliente"].dtype != ventas["id_cliente"].dtype:
        print("[validación] ERROR: id_cliente tiene tipos distintos.")
        ok = False
    else:
        print(f"[validación] OK: mismo tipo de dato ({ventas['id_cliente'].dtype}).")

    # 4.
    sin_cliente = (~ventas["id_cliente"].isin(clientes["id_cliente"])).sum()
    print(f"[validación] Ventas sin cliente asociado: {sin_cliente}")

    return ok


def unir(clientes, ventas):
    """Une ventas con clientes usando "id_cliente" y guarda el resultado en Data/processed/merge.csv.

    Pistas:
    - Usar pd.merge(...) o ventas.merge(...).
    - Usar how="left" para no perder ventas.
    - Usar validate="m:1" para confirmar que cada venta tiene un solo cliente.
    - Guardar con df.to_csv(...) en PROCESSED / "merge.csv".
    """
    # TODO 7: validar con validar_premerge(), hacer el merge, guardar el CSV y devolver el dataframe.

    if not validar_premerge(clientes, ventas):
        print("No se puede hacer el merge: corrija los errores de validación.")
        return None

    df = ventas.merge(clientes, on="id_cliente", how="left", validate="m:1")

    PROCESSED.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED / "merge.csv", index=False)

    print(f"Ventas: {ventas.shape} | Clientes: {clientes.shape} | Merge: {df.shape}")
    print(f"Guardado en {PROCESSED / 'merge.csv'}")

    return df
    
 